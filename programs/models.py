from django.db import models

# Create your models here.

class Degree(models.Model):
    level = models.IntegerField(choices=DegreeLevel.choices, default=DegreeLevel.NONE)
    specialty = models.IntegerField(choices=DegreeSpecialty.choices, default=DegreeSpecialty.NONE)
    format = models.IntegerField(choices=ProgramFormat.choices, default=ProgramFormat.NONE)
    id = 0
    name = ""


class ScheduleType(models.IntegerChoices):
    NONE = 0
    PART_TIME = 1
    FULL_TIME = 2

class DormRequirement(models.IntegerChoices):
    NONE = 0
    REQUIRED = 1
    OPTIONAL = 2

class DormAvailability(models.IntegerChoices):
    NONE = 0
    AVAILABLE = 1
    LIMITED = 2
    UNAVAILABLE = 3

class ProgramProfile(models.Model):
    program_id = models.IntegerField(default=0)
    degree = Degree()
    schedule = models.IntegerField(choices=ScheduleType.choices, default=ScheduleType.NONE)
    tuition = models.FloatField(default=0.0)
    dorm_requirement = models.IntegerField(choices=DormRequirement.choices, default=DormRequirement.NONE)
    dorm_availability = models.IntegerField(choices=DormAvailability.choices, default=DormAvailability.NONE)
    acceptance_rate = models.BooleanField(default=False)
    esl_support = models.BooleanField(default=False)
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    # def __init__(self, degree, schedule, tuition, dorm_requirement, dorm_availability, acceptance_rate, esl_support, school, program_id):
    #     self.degree = degree
    #     self.schedule = schedule
    #     self.tuition = tuition
    #     self.dorm_requirement = dorm_requirement
    #     self.dorm_availability = dorm_availability
    #     self.acceptance_rate = acceptance_rate
    #     self.esl_support = esl_support
    #     self.program_id = program_id
    #     # TODO: figure out how to set school based on program ID

    def get_degree_level(self):
        return self.degree.level
    
    def get_degree_specialty(self):
        return self.degree.specialty
    
    def get_degree_format(self):
        return self.degree.format
    
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
    id = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True)
    approval_status = models.BooleanField(default=False)
    matched_students = models.JSONField(default=list)
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    program_profile = ProgramProfile()

    # def __init__(self, name, id, school, program_profile):
    #     self.name = name
    #     self.id = id
    #     self.school = school
    #     self.program_profile = program_profile

    def __str__(self):
        return (f"{self.name} at {self.school}, ID {self.id}\nApproved: {self.approval_status}")

    def get_program_stats():
        return dict() # TODO: figure out what to return

    def get_profile(self):
        return self.program_profile