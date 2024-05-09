from django.urls import path
from . import views
urlpatterns = [
    path("", views.Boneless),
    path("boneless",views.Boneless)
]
