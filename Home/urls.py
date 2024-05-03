from django.urls import path
from . import views
urlpatterns = [
    path("", views.Homes),
    path("Home", views.Homes)
]
