from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenge_int),
    path("<str:month>", views.monthly_challenges, name="monthly-challenge"),
    
    
]
