from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reaction/leaderboard', views.leaderboard, name='leaderboard'),
    path('reaction', views.reaction, name='reaction'),

]
