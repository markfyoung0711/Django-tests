from django.db import models

# Create your models here.

# Models for User, Student, Course, Enrollment

# User


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Student(User):
    pass


class Course(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=20)


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, null=True)
    date = models.DateField()
