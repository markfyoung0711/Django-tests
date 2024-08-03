# Django - Student/Class

## Requirements.

### Overview:
#### Basics
1. Create Students
1. Create Courses
1. Assign Courses to Students
1. Print Report
#### Advanced
1. Manage Schedule of Course
1. Manage Status of Course
1. Manage Status of Student
#### Advanced 2
1. Payment/Cost
1. Discount



### GUI

#### Basic
Login
Create Student
Create Course
Student Signup for Course


### Objects:
1. Student
    behavior: modify, deactivate, delete.
    attributes: student_id, name, dob, status

2. Create Course 
    behavior: modify, deactivate, schedcule, delete.
    attributes: course_id, name, description, date, time, cost, status (schedule - advanced)

3. Schedule
    operates like a calendar, but what are the differences from a calendar
    behavior: view, whitelist, blacklist
    attributes: date, time
    examples: winter schedule, fall, etc., holidays

### Design Steps
1. start with GUI screens as HTML templates ( See # Design Approach below)
2. create DB tables in SQLite to handle User, Student, Course, Enrollment
3. create classes for basics
4. write cli version of application
5. write API for doing the functions/behaviors that can be done at command line

# Design Approach.
A top-down approach to developing a web app, where the GUI is developed first, can be an effective way to ensure that the user interface and user experience drive the design and development process. Here's a basic outline to help you get started with your project using Django:

### Step 1: Design the GUI
1. **Wireframes and Mockups**: Create wireframes and mockups of your application's main pages, such as the login page, student creation page, course creation page, and course assignment page. Tools like Figma, Sketch, or Adobe XD can be useful for this purpose.

2. **HTML/CSS Templates**: Convert your wireframes into HTML/CSS templates. Use a front-end framework like Bootstrap or Tailwind CSS to speed up development and ensure a responsive design.

### Step 2: Set Up Your Django Project
1. **Create a Django Project**:
    ```bash
    django-admin startproject school_management
    cd school_management
    ```

2. **Create a Django App**:
    ```bash
    python manage.py startapp core
    ```

3. **Integrate Your HTML/CSS Templates**: Place your HTML templates in the `templates` directory of your app and static files (CSS, JS, images) in the `static` directory.

### Step 3: Develop the Backend Logic
1. **Define Models**:
    ```python
    from django.db import models
    from django.contrib.auth.models import AbstractUser

    class User(AbstractUser):
        email = models.EmailField(unique=True)
        is_verified = models.BooleanField(default=False)
        verification_code = models.CharField(max_length=6, blank=True, null=True)

    class Student(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)

    class Course(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()

    class Enrollment(models.Model):
        student = models.ForeignKey(Student, on_delete=models.CASCADE)
        course = models.ForeignKey(Course, on_delete=models.CASCADE)
    ```

2. **Create Forms**:
    ```python
    from django import forms
    from .models import User, Student, Course

    class UserForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['email']

    class StudentForm(forms.ModelForm):
        class Meta:
            model = Student
            fields = ['first_name', 'last_name']

    class CourseForm(forms.ModelForm):
        class Meta:
            model = Course
            fields = ['name', 'description']
    ```

3. **Set Up Views**:
    ```python
    from django.shortcuts import render, redirect
    from .forms import UserForm, StudentForm, CourseForm
    from .models import Student, Course, Enrollment
    from django.core.mail import send_mail
    import random

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
        return render(request, 'login.html', {'form': form})

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

    def create_student(request):
        if request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('student_list')
        else:
            form = StudentForm()
        return render(request, 'create_student.html', {'form': form})

    def create_course(request):
        if request.method == 'POST':
            form = CourseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('course_list')
        else:
            form = CourseForm()
        return render(request, 'create_course.html', {'form': form})
    ```

4. **URLs Configuration**:
    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('login/', views.login_view, name='login'),
        path('verify/', views.verify_view, name='verify'),
        path('create_student/', views.create_student, name='create_student'),
        path('create_course/', views.create_course, name='create_course'),
    ]
    ```

### Step 4: Connect Frontend and Backend
1. **Integrate Forms with Templates**: Embed Django forms in your HTML templates and ensure that form submissions are correctly handled by your views.

2. **Add User Authentication**: Use Django's built-in authentication system to handle user sessions and access control.

### Step 5: Testing and Deployment
1. **Test Your Application**: Ensure that all functionalities, such as student creation, course creation, course assignment, and email verification, work as expected.

2. **Deploy Your Application**: Use a deployment platform like Heroku, AWS, or DigitalOcean to deploy your Django application.

By following this top-down approach, you can ensure that the user interface is at the forefront of your development process, which can help create a more intuitive and user-friendly application.

# Design Systems UI/UX

There are several free Figma component libraries that provide ready-made components suitable for building a web application for entering Student, Course, and Enrollment data. Here are a few options:

### 1. **Ant Design System for Figma**
Ant Design is a popular React UI library that provides a comprehensive set of components. There is a Figma library available that mirrors these components, which can be very useful for designing your application.

- **Figma Library**: [Ant Design System for Figma](https://www.figma.com/community/file/809545734658213423)
- **Features**: Includes components such as forms, tables, buttons, modals, and more.

### 2. **Material Design System**
Material Design is a design language developed by Google. It provides a wide range of components that can be used to build modern web applications.

- **Figma Library**: [Material Design System](https://www.figma.com/community/file/845846322346154300)
- **Features**: Offers a variety of components, including inputs, buttons, cards, and data tables.

### 3. **Tailwind UI Kit**
Tailwind CSS is a utility-first CSS framework, and there are several Figma kits available that offer pre-designed components based on Tailwind CSS.

- **Figma Library**: [Tailwind UI Kit](https://www.figma.com/community/file/768809027799962739)
- **Features**: Provides form elements, buttons, cards, tables, and more, all styled according to Tailwind CSS principles.

### 4. **Bootstrap Grid and UI Kit**
Bootstrap is a widely-used CSS framework, and there are Figma kits that offer Bootstrap-based components.

- **Figma Library**: [Bootstrap Grid and UI Kit](https://www.figma.com/community/file/972874993265392002)
- **Features**: Includes forms, buttons, tables, modals, and other common UI elements.

### 5. **Eva Design System**
Eva Design System is a customizable design system that provides a range of components suitable for enterprise applications.

- **Figma Library**: [Eva Design System](https://www.figma.com/community/file/804445633684802264)
- **Features**: Includes input fields, buttons, tables, cards, and more.

### How to Use These Libraries
1. **Import the Library**: Open the link to the Figma community file and click "Duplicate" to add it to your own Figma account.
2. **Customize Components**: Tailor the components to match your application's branding and requirements.
3. **Export HTML/CSS**: Use the Figma designs as a reference to implement the HTML and CSS in your Django application.

These component libraries will provide a strong starting point for your UI design, making it easier to focus on the functionality and user experience of your web application.
