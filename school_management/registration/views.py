import random

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from registration.models import User, Student, Course, Enrollment
from .forms import UserForm, StudentForm, CourseForm


# Create your views here.

# each function added here will render an html page using django render

# for each of the view functions below...
# TODO: what is the dictionary for as the last argument?
# note: the <app>/home.html file will need to be hand-created.
# as a template


def generate_verification_code():
    return str(random.randint(100000, 999999))


def send_verification_email(user):
    code = generate_verification_code()
    user.verification_code = code
    user.save()
    send_mail(
        'Your Verification Code',
        f'Your verification code is {code}',
        'from@example.com',
        [user.email],
    )


def login_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password('temporarypassword')
            user.save()
            send_verification_email(user)
            return redirect('verify')
    else:
        form = UserForm()
    return render(request, 'registration/login.html', {'form': form})


def verify_view(request):
    if request.method == 'POST':
        code = request.POST['code']
        try:
            user = User.objects.get(verification_code=code)
            user.is_verified = True
            user.save()
            return redirect('home')
        except User.DoesNotExist:
            pass
    return render(request, 'verify.html')


def home(request):
    return render(request, "registration/home.html", {})


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'registration/create_user.html', {'form': form})


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'registration/create_course.html', {'form': form})


def create_enrollment(request):
    return render(request, "registration/create_enrollment.html", {})


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'registration/create_student.html', {'form': form})


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


def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    context = {
        "course": course
    }
    return render(request, "registration/course_detail.html", context)


def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    context = {
        "student": student
    }
    return render(request, "registration/student_detail.html", context)


def enrollment_detail(request, pk):
    enrollment = Enrollment.objects.get(pk=pk)
    context = {
        "enrollment": enrollment
    }
    return render(request, "registration/enrollment_detail.html", context)
