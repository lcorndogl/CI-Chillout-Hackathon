from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('delete-score/<int:score_id>/', views.delete_score, name='delete_score'),
    path('', views.home, name='home'),
    path('reaction/leaderboard', views.leaderboard, name='leaderboard'),
    path('reaction', views.reaction, name='reaction'),
    path('manage', views.reaction, name='manage'),
    path('save-reaction-time/', views.save_reaction_time, name='save_reaction_time'),
]
