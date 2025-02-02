from django.shortcuts import render
# , get_object_or_404, reverse, redirect
# from django.views import generic
from django.contrib import messages
# from django.http import HttpResponseRedirect
from .forms import ScoresForm

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

    score = ScoresForm()
    if request.method == "POST":
        score = ScoresForm(data=request.POST)
        if score.is_valid():
            scores = score.save(commit=False)
            scores.user = request.user
            scores.score = score.cleaned_data['score']
            scores.save()
            messages.success(request, 'Score saved successfully')
    context = {
        'scores_form': score
    }

    return render(
        request,
        "reactions/reaction.html",
        context,
    )


def leaderboard(request):
    """
    Displays the home page
    """
    return render(
        request,
        "reactions/leaderboard.html",
    )
