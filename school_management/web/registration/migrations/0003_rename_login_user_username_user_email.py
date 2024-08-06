# Generated by Django 5.0.7 on 2024-08-03 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0002_enrollment_course_enrollment_student"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="login",
            new_name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.CharField(default="undefined@undefined.com", max_length=100),
            preserve_default=False,
        ),
    ]