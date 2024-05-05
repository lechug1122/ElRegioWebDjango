from django.urls import path
from . import views
urlpatterns = [
    path("", views.logins),
    path("login", views.logins)
]
