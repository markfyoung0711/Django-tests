# registration/urls.py

from django.urls import path

# app references to view functions
from registration import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login_view"),
    path("create_student/", views.create_student, name="create_student"),
    path("create_course/", views.create_course, name="create_course"),
    path("create_enrollment/", views.create_enrollment, name="create_enrollment"),

    path("<int:pk>", views.student_detail, name="student_detail"),
    path("<int:pk>", views.course_detail, name="course_detail"),
    path("<int:pk>", views.enrollment_detail, name="enrollment_detail"),

    path("student_index/", views.student_index, name="student_index"),
    path("course_index/", views.course_index, name="course_index"),
    path("enrollment_index/", views.enrollment_index, name="enrollment_index"),
]
