from django.shortcuts import render

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
