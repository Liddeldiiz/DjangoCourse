from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    date_modified = models.DateField(auto_now=True)

    def get_Fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_Fullname()
    
class Tag(models.Model):
    caption = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField()
    image_name = models.CharField(max_length=80)
    date = models.DateField()
    date_modified = models.DateField(auto_now=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    content = models.TextField(default="", null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    #author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    caption = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("post-detail", args=[self.slug])
    

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title