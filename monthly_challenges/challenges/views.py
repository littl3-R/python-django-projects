from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

monthly_challenges = {
    "january": "Don't eat meat for the entire month!",
    "february": "Walk for at least 30 minutes every day!",
    "march": "Write a django app per day!",
    "april": "Buy a new monitor!",
    "may": "Swim!",
    "june": "Write some code!",
    "july": "Don't eat meat for the entire month!",
    "august": "Walk for at least 30 minutes every day!",
    "september": "Write a django app per day!",
    "october": "Buy a new monitor!",
    "november": "Swim!",
    "december": "Write some code!",
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month]
    )  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
