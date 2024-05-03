#librerias

from django.urls import path
from .import views

urlpatterns = [
    path("", views.Registers),
    path("Register",views.Registers)
]
