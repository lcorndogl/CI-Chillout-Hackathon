from django.shortcuts import render, redirect
# , get_object_or_404, reverse, redirect
# from django.views import generic
from django.contrib import messages
# from django.http import HttpResponseRedirect
from .forms import ScoresForm, ScoreForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Score
import json

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
    Displays the leaderboard page
    """
    top_scores = Score.objects.filter(hidden=False).order_by('score')[:25]
    context = {
        'top_scores': top_scores
    }
    return render(
        request,
        "reactions/leaderboard.html",
        context,
    )

@csrf_exempt
@login_required
def save_reaction_time(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        score = data.get('score')
        if score is not None:
            Score.objects.create(user=request.user, score=score)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def profile(request):
    """
    Displays the profile page with the user's scores
    """
    user_scores = Score.objects.filter(user=request.user).order_by('score')
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            score_id = request.POST.get('score_id')
            score = Score.objects.get(id=score_id, user=request.user)
            score.hidden = form.cleaned_data['hidden']
            score.save()
            return redirect('profile')
    else:
        form = ScoreForm()
    context = {
        'user_scores': user_scores,
        'form': form
    }
    return render(request, "reactions/profile.html", context)

@login_required
def delete_score(request, score_id):
    """
    Deletes a score from the user's profile
    """
    score = Score.objects.get(id=score_id, user=request.user)
    if score:
        score.delete()
        return redirect('profile')
    return redirect('profile')
