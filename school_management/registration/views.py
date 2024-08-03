from django.shortcuts import render
from registration.models import User, Student, Course, Enrollment

# Create your views here.

# each function added here will render an html page using django render

# for each of the view functions below...
# TODO: what is the dictionary for as the last argument?
# note: the <app>/home.html file will need to be hand-created.
# as a template


def home(request):
    return render(request, "registration/home.html", {})


def login(request):
    return render(request, "registration/login.html", {})


def user(request):
    return render(request, "registration/user.html", {})


def course(request):
    return render(request, "registration/course.html", {})


def enrollment(request):
    return render(request, "registration/enrollment.html", {})


def student(request):
    return render(request, "registration/student.html", {})


def course_index(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, "registration/course_index.html", context)


def student_index(request):
    students = Student.objects.all()
    context = {
        "students": students
    }
    return render(request, "registration/student_index.html", context)


def user_index(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, "registration/user_index.html", context)


def enrollment_index(request):
    enrollments = Enrollment.objects.all()
    context = {
        "enrollments": enrollments
    }
    return render(request, "registration/enrollment_index.html", context)
