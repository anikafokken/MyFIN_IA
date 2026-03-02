from enum import Enum
from django.db import models
import sys
print(sys.executable)
from django.dispatch import receiver
from django.db.models.signals import post_save
import geopy
from geopy.geocoders import Nominatim
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
import abc
from django.contrib.gis.measure import Distance, D
from geopy.distance import distance
from core import constants

from core.constants import DegreeLevel

class AbstractModelMeta(abc.ABCMeta, type(models.Model)):
    pass

    
class CustomUser(AbstractUser):
    class AccountType(models.TextChoices):
        STUDENT = "STUDENT"
        SCHOOL = "SCHOOL"
        ADMIN = "ADMIN"
        
    FIRST_NAME_FIELD = "first_name"
    LAST_NAME_FIELD = "last_name"
    USERNAME_FIELD = "username"
    PASSWORD_FIELD = "password"
    EMAIL_FIELD = "email"
    school_name = models.CharField(max_length=20, default="", blank=True)
    # admin_code = models.CharField(max_length=20, default="", blank=True)
    account_type = models.CharField(
        max_length=20,
        choices=AccountType.choices, 
        default=AccountType.STUDENT)
    REQUIRED_FIELDS = []

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.username}, {self.account_type}"

class School(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="school_profile")
    name = models.CharField(max_length=255, blank=True)
    is_private = models.BooleanField(default=False)
    program_list = models.JSONField(default=list)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, default='0')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, default='0')
    # coordinates = models.JSONField(latitude, longitude, default=tuple)
    # location = models.PointField(geography=True, dim=2, srid=4326)
    


    # def __init__(self, name, id, program_list=list()):
    #     self.program_list = program_list
    #     self.id = id
    #     self.name = name

    # def __str__(self):
    #     return f"{self.name}, ID {self.id}"

    # def add_program(self, program):
    #     return


# class Factor(models.Model):
#     program_attribute = models.JSONField()
#     scoring_weight = models.FloatField(default=0)
#     class ConstraintType(models.TextChoices):
#         HARD = "HARD"
#         SOFT = "SOFT"
#     constraint_type = models.CharField(max_length=10, choices=ConstraintType.choices, default="SOFT")
    
#     def set_scoring_weight(self):
#         # get weights data from database
#         weights = Factor.objects.all() # probably not right
        

class Location(models.Model):
    coordinates = models.JSONField(default=tuple)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, default='0')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, default='0')

    geolocator = Nominatim(user_agent="MyFIN_IA")


    # def __init__(self, coordinates):
    #     self.coordiantes = coordinates

    def get_city_info(self, address):
        geolocator = Nominatim(user_agent="MyFIN_IA")

        location = geolocator.geocode(address)
        if location:
            print(location)
            return location
        else:
            print("Location not found")

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_profile")
    name = models.CharField(max_length=255, blank=True)
    desired_program_types = models.JSONField(default=list) # may need to change to ArrayField when adding in ProgestreSQL, list of Degree Specialties
    matched_list = models.JSONField(default=list) # of programs
    confirmed_matches = models.JSONField(default=list) # of programs
    degree_level = models.IntegerField(choices=DegreeLevel.choices, default=DegreeLevel.NONE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, default='0')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, default='0')
    # coordinates = models.JSONField(latitude, longitude, default=tuple)
    # location = models.PointField(geography=True, dim=2, srid=4326)
    max_tuition = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    degree_level_factor = models.IntegerField(choices=constants.ScheduleType)
    schedule_type_factor = models.IntegerField(choices=constants.ScheduleType)
    degree_specialty_factor = models.IntegerField(choices=constants.DegreeSpecialty)
    esl_support_factor = models.IntegerField(choices=constants.ESLSupportAvailability)
    dorm_requirement_factor = models.IntegerField(choices=constants.DormRequirement)
    dorm_availability_factor = models.IntegerField(choices=constants.DormAvailability)


    # def __init__(self, name, id, goal_prog_types, degree_level):
    #     self.name = name
    #     self.id = id
    #     self.desired_program_types = goal_prog_types
    #     self.degree_level = degree_level
        
    # def __str__(self):
    #     return (f"{self.name}, ID {self.id}")
    
    def get_program_types(self):
        return self.desired_program_types

    def get_matched_list(self):
        return self.matched_list

    def get_confirmed_matches(self):
        return self.confirmed_matches
    
    def set_program_types(self, new_types):
        self.desired_program_types = new_types
    
    def add_match(self, program):
        self.matched_list.append(program)
    
    # @property
    # def distance_to(self, school: School):
    #     distance = Distance(m=distance(self.location, school.location).meters)

class MatchManager(models.Model):
    success_rate = models.FloatField(default=0.0)
    past_matches = models.JSONField(default=dict)

    # def __init__(self, past_matches=None):
    #     if past_matches is not None:
    #         self.past_matches = past_matches

    def get_success_rate():
        return 0


# prevent crashing
@receiver(post_save, sender=settings.AUTH_USER_MODEL) # watchs for changes in database, especially after a save
def manage_student_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

