from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import Post

# Create your views here.

def get_date(post):
    return post['date']

def index(request):
    posts = Post.objects.all()

    return render(request, 'blog/index.html', {
        "posts": posts
    })

def posts(request):
    #post_keys = list(posts_content.keys())
    posts = Post.objects.all()
    return render(request, 'blog/all-posts.html', {
        "posts": posts
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    #identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": post
    })
