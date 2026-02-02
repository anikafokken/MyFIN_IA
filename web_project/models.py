from enum import Enum
from django.db import models

class Student(models.Model):
    id = 1
    name = ""
    # desired_program_types
    # constraints
    # preferences
    # matched_list
    # confirmed_matches

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return self.title
    
class School(models.Model):
    is_private = False
    program_list = list()
    # location

    def __init__(self, id, program_list=list()):
        self.program_list = program_list
        self.id = id

    def add_program(program):
        print(program)

class Program(models.Model):
    id = 0
    approval_status = False
    matched_students = list()
    school = School()
    # program_profile

class ProgramProfile(models.Model):
    # degree
    # schedule
    tuition = 0.0
    # dorm_requirement
    # dorm_availability
    acceptance_rate = 0.0
    esl_support = False
    school = School()

class Degree(models.Model):
    # level
    # specialty
    # format
    id = 0

class DegreeLevel(Enum):
    PRACTICAL_NURSING = 1
    ASN = 2
    BSN = 3
    BSN_PRELIC = 4
    GRAD_CERT = 5
    MSN = 6
    MSN_PRELIC = 7
    DNP = 8
    PHD = 9


class ScheduleType(Enum):
    PART_TIME = 1
    FULL_TIME = 2

class DormRequirement(Enum):
    REQUIRED = 1
    OPTIONAL = 2

class DormAvailability(Enum):
    AVAILABLE = 1
    LIMITED = 2
    UNAVAILABLE = 3