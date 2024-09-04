from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the whole month",
    "february": "Walk for at least 20 min every day",
    "march": "Learn Django for at least 20 min every day",
    "april": "Eat no vegtables for the whole month",
    "may": "Run for at least 20 min every day",
    "june": "Learn Python for at least 20 min every day",
    "july": "Eat no chocolate for the whole month",
    "august": "Hike for at least 40 min every day",
    "september": "Learn Data Science for at least 20 min every day",
    "october": "Eat no Fast Food for the whole month",
    "november": "Drive on a Bike for at least 40 min every day",
    "december": None
}

# Learn OSINT for at least 20 min every day

# Create your views here.

def index(reqeuest):
    months = list(monthly_challenges.keys())

    return render(reqeuest, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def  monthly_challenge(request, month):
    try:
        
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": challenge_text
        })
    except:
        raise Http404()