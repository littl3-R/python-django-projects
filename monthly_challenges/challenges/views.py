from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
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
    "december": None,
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


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
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month": month},
        )
    except:
        raise Http404()
