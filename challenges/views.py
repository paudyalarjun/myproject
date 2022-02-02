from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

challenges_month = {
    "january": "Do 20 push-ups everyday!",
    "february": "The work for February is sleep 7 and half hours per day!",
    "march": "Watch movies of different languages every week!",
    "april": "Do not use Social Media!",
    "may": "Visit new places every week!",
    "june": "Help peoples in need!",
    "july": "Walk at least 2 km every day!",
    "august": "Eat Healthy Everyday!",
    "september": "Drink at least 2.5 litre water everyday!",
    "october": "Celebrate the whole month!",
    "november": "NNN!",
    "december": "Stay Warm because this is the month of winter!"
}

# Create your views here.



def monthly_challenge_int(request, month):
    months = list(challenges_month.keys())

    if month > len(months) or month == 0:
        return HttpResponseNotFound("Invalid input. Enter the valid number of month!")
    else:
        months_redirect = months[month - 1]
        redirect_path = reverse("monthly-challenge", args = [months_redirect])
        return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = challenges_month[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Invalid input. Enter the name of valid month!</h1>")














"""
def monthly_challenge_int(request, month):
    months = list(challenges_month.keys())
    if month > len(months) or month == 0:
        return HttpResponseNotFound("Invalid input. Enter the name of valid month!")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenges(request, month):
    try:
        challenge_text = challenges_month[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Invalid input. Enter the name of valid month!")
"""




    
