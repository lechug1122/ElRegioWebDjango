from django.urls import path
from . import views

urlpatterns = [
    path("", views.Nosostros),
    path("combos", views.Nosostros)
]
