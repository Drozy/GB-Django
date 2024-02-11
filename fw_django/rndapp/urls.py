from django.urls import path
from . import views

urlpatterns = [
    path('coin/', views.coin, name='coin'),
    path('coin/<int:count>/', views.coin, name='coin'),
    path('dice/', views.dice, name='dice'),
    path('dice/<int:count>/', views.dice, name='dice'),
    path('num/', views.rnd_num, name='rnd_num'),
    path('num/<int:count>/', views.rnd_num, name='rnd_num'),
    path('game/', views.game_choice, name='game_choice'),
]
