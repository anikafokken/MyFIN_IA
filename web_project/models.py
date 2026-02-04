from enum import Enum
from django.db import models
import sys
print(sys.executable)
import geopy
from geopy.geocoders import Nominatim

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

class Degree(models.Model):
    level = DegreeLevel()
    specialty = DegreeSpecialty()
    format = ProgramFormat()
    id = 0

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
    
class School(models.Model):
    name = ""
    id = int()
    is_private = bool()
    program_list = list()
    # location

    def __init__(self, name, id, program_list=list()):
        self.program_list = program_list
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.name}, ID {self.id}"

    def add_program(self, program):
        self.program_list.append(program)

class Location(models.Model):
    coordinates = tuple()

    def __init__(self, coordinates):
        self.coordiantes = coordinates

    def get_city_info(coordinates):
        latitude = coordinates[0]
        longitude = coordinates[1]

        geolocator = Nominatim(user_agent="MyFIN_IA")
        location = geolocator.geocode("1015 Snelling Ave S Saint Paul, 55116")
        print(location.address)

class ProgramProfile(models.Model):
    program_id = int()
    degree = Degree()
    schedule = ScheduleType()
    tuition = float()
    dorm_requirement = DormRequirement()
    dorm_availability = DormAvailability()
    acceptance_rate = float()
    esl_support = bool()
    school = School()

    def __init__(self, degree, schedule, tuition, dorm_requirement, dorm_availability, acceptance_rate, esl_support, school, program_id):
        self.degree = degree
        self.schedule = schedule
        self.tuition = tuition
        self.dorm_requirement = dorm_requirement
        self.dorm_availability = dorm_availability
        self.acceptance_rate = acceptance_rate
        self.esl_support = esl_support
        self.program_id = program_id
        # TODO: figure out how to set school based on program ID

    def get_degree_type(self):
        return
    
    def get_schedule(self):
        return self.schedule
    
    def get_tuition(self):
        return self.tuition
    
    def get_dorm_requirement(self):
        return self.dorm_requirement
    
    def get_dorm_availability(self):
        return self.dorm_availability
    
    def get_acceptance_rate(self):
        return self.acceptance_rate
    
    def get_esl_support(self):
        return self.esl_support
    
    def get_school(self):
        return self.school

class Program(models.Model):
    id = int()
    name = ""
    approval_status = bool()
    matched_students = list()
    school = School()
    program_profile = ProgramProfile()

    def __init__(self, name, id, school, program_profile):
        self.name = name
        self.id = id
        self.school = school
        self.program_profile = program_profile

    def __str__(self):
        return (f"{self.name} at {self.school}, ID {self.id}\nApproved: {self.approval_status}")

    def get_program_stats():
        return dict() # TODO: figure out what to return

    def get_profile(self):
        return self.program_profile

class Student(models.Model):
    id = int()
    name = str()
    desired_program_types = list(Degree)
    # constraints
    # preferences
    matched_list = list(Program)
    confirmed_matches = list(Program)

    def __init__(self, name, id, goal_prog_types):
        self.name = name
        self.id = id
        self.desired_program_types = goal_prog_types
        
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
    success_rate = float()
    past_matches = dict()

    def __init__(self, past_matches=None):
        if past_matches is not None:
            self.past_matches = past_matches

    def get_success_rate():
        return 0