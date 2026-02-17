from enum import Enum
from django.db import models
import sys
print(sys.executable)
import geopy
from geopy.geocoders import Nominatim

from core.constants import DegreeLevel
    
class School(models.Model):
    name = models.CharField(max_length=255, blank=True)
    is_private = models.BooleanField(default=False)
    program_list = models.JSONField(default=list)
    # location

    # def __init__(self, name, id, program_list=list()):
    #     self.program_list = program_list
    #     self.id = id
    #     self.name = name

    def __str__(self):
        return f"{self.name}, ID {self.id}"

    # def add_program(self, program):
    #     return

class Location(models.Model):
    coordinates = models.JSONField(default=tuple)

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
    name = models.CharField(max_length=255, blank=True)
    desired_program_types = models.JSONField(default=list) # may need to change to ArrayField when adding in ProgestreSQL, list of Degree Specialties
    # constraints
    # preferences
    matched_list = models.JSONField(default=list) # of programs
    confirmed_matches = models.JSONField(default=list) # of programs
    degree_level = models.IntegerField(choices=DegreeLevel.choices, default=DegreeLevel.NONE)

    # def __init__(self, name, id, goal_prog_types, degree_level):
    #     self.name = name
    #     self.id = id
    #     self.desired_program_types = goal_prog_types
    #     self.degree_level = degree_level
        
    def __str__(self):
        return (f"{self.name}, ID {self.id}")
    
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

class MatchManager(models.Model):
    success_rate = models.FloatField(default=0.0)
    past_matches = models.JSONField(default=dict)

    # def __init__(self, past_matches=None):
    #     if past_matches is not None:
    #         self.past_matches = past_matches

    def get_success_rate():
        return 0