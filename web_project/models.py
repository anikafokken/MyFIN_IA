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
    # is_private
    program_list = list()
    # location

    def __init__(self, id, program_list=list()):
        self.program_list = program_list
        self.id = id

    def add_program(program):
        print(program)

# class Program(models.Model):
    



# class ProgramProfile(models.Model