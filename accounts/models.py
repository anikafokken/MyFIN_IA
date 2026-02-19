from django.db import models
from django.conf import settings

# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_profile")
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    grade_level = models.IntegerField() # might need to be an enum instead

class SchoolProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="school_profile")
    location = models.ForeignKey('users.Location', on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255)
    application_website = models.URLField()