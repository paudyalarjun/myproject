from http.client import HTTPResponse
from os import sep
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
    "october": None,
    "november": "NNN!",
    "december": "Stay Warm because this is the month of winter!"
}

# Create your views here.


def index(request):
    #list_items = ""
    months = list(challenges_month.keys())

    #for month in months:
    #    response_url = reverse("monthly-challenge", args=[month])

    #    capitalized_months = month.capitalize()
    #    list_items += f"""<li> <a href = "{response_url}"> {capitalized_months} </a> </li>"""
    
    #return_list = f"<ul style=\"list-style-type:none;\">{list_items}</ul>"

    return render(request, "challenges/index.html", {
        "show_months": months,
    })


def monthly_challenge_int(request, month):
    months = list(challenges_month.keys())

    if month > len(months) or month == 0:
        raise Http404()
    
    months_redirect = months[month - 1]
    redirect_path = reverse("monthly-challenge", args = [months_redirect])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = challenges_month[month]

        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })

        # response_data = f"<h1>{challenge_text}</h1>"
        # return HttpResponse(response_data)
    except:
        raise Http404()
















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




    
