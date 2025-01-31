from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    """
    Displays the home page
    """
    return render(
        request,
        "reactions/index.html",
    )


def reaction(request):
    """
    Displays the home page
    """
    return render(
        request,
        "reactions/reaction.html",
    )


def leaderboard(request):
    """
    Displays the home page
    """
    return render(
        request,
        "reactions/leaderboard.html",
    )
