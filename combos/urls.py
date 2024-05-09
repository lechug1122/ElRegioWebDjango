from django.urls import path
from . import views

urlpatterns = [
    path("", views.Combos1),
    path("combos", views.Combos1)
]
