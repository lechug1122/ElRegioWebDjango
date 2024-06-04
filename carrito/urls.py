from django.urls import path
from . import views

urlpatterns = [
    path("", views.Carritos),
    path("combos", views.Carritos)
]
