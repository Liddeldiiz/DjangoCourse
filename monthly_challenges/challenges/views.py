from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the whole month",
    "february": "Walk for at least 20 min every day",
    "march": "Learn Django for at least 20 min every day",
    "april": "Eat no meat for the whole month",
    "may": "Eat no meat for the whole month",
    "june": "Eat no meat for the whole month",
    "july": "Eat no meat for the whole month",
    "august": "Eat no meat for the whole month",
    "september": "Eat no meat for the whole month",
    "october": "Eat no meat for the whole month",
    "november": "Eat no meat for the whole month",
    "december": "Eat no meat for the whole month"
}

# Create your views here.

def challenges(reqeuest):
    list_elements = ''
    for month in list(monthly_challenges.keys()):

        #redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[month])
        print(redirect_path)
        list_elements += f'<li><a href={redirect_path}>{month}</a></li>'
    response_data = f'<ul>{list_elements}</ul>'
    return HttpResponse(response_data)

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
        response_data = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_data)
    except:
        HttpResponseNotFound("<h1>This Month is not supported!</h1>")