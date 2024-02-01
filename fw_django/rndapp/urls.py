from django.urls import path
from . import views

urlpatterns = [
    path('coin/', views.coin, name='coin'),
    path('dice/', views.dice, name='dice'),
    path('num/', views.rnd_num, name='rnd_num'),
]
