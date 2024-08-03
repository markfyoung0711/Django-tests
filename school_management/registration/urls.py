# registration/urls.py

from django.urls import path

# app references to view functions
from registration import views

urlpatterns = [
    path("", views.home, name="home"),
    path("", views.login, name="login"),
    path("", views.user, name="user"),
    path("", views.student, name="student"),
    path("", views.course, name="course"),
    path("", views.enrollment, name="enrollment"),
]
