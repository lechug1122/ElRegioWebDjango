from django.urls import path
from . import views
urlpatterns = [
    path("", views.Samplers),
    path("Samplers", views.Samplers)
]
