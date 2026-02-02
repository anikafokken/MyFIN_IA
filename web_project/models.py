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

class ProgramFormat(Enum):
    TRADITIONAL = 1
    ACCELERATED = 2
    BRIDGE = 3
    POST_BACC = 4
    N_A = 5

class DegreeSpecialty(Enum):
    ADULT_GERON_ACUTE = 1
    ADULT_GERON_PRIM = 2
    ADULT_GERON_CLIN_SPEC = 3
    FAMILY_NP = 4
    HEALTH_IT = 5
    MIDWIFERY = 6
    NURSING_ADMIN_LEAD = 7
    NURSE_EDU = 8
    PED_CLIN_SPEC = 9
    PED_ACU_NP = 10
    PSYCH_NP = 11
    WOMENS_HEALTH_NP = 12
    TRANSCULTURAL = 13
    INNOVATIONS = 14
    INTEG_HEALING = 15
    NEONAT_NP = 16
    NURSE_ANESTH = 17
    PUBLIC_HEALTH = 18
    NURSING_PROMOTION = 19
    CHRONIC_COND_PREV = 20
    POP_HEALTH = 21
    SYMPT_MANAGEMENT = 22
    NONE = 23

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

class ProgramProfile(models.Model):
    # degree
    # schedule
    tuition = 0.0
    dorm_requirement = DormRequirement.OPTIONAL
    dorm_availability = DormAvailability.UNAVAILABLE
    acceptance_rate = 0.0
    esl_support = False
    school = School()