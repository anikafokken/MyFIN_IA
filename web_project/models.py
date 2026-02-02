from django.db import models

class Student(models.Model):
    id = 1
    name = "Anika Fokken"
    # desired_program_types
    # constraints
    # preferences
    # matched_list
    # confirmed_matches

    def __str__(self):
        return self.title
    
class School(models.Model):


class Program(models.Model):
    



class ProgramProfile(models.Model)