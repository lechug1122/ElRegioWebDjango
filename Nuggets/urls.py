from django.urls import path
from . import views
urlpatterns = [
    path("",view=views.nuggets),
    path("Nuggets", views.nuggets)
]
