from django.db import models
import heapq
from programs.models import Program
from abc import ABC, abstractmethod
from core.constants import DegreeLevel
from factors import NumericPreferenceFactor, ComparisonConstraint, UserRule, SelectionPreferenceFactor
from users.models import Student, CustomUser
from core import settings
from django.http import HttpRequest
import operator

top_ten = []

assignment = {
    "student": None,
    "program": None
}

def build_engine_components(user_rules: list[UserRule]):
    constraints = []
    preferences = []

    for rule in user_rules:
        if rule.mode == "HARD":
            constraints.append(ComparisonConstraint(rule.extractor, rule.operator))
        elif rule.mode == "SOFT":
            if rule.data_type == "NUMERIC":
                preferences.append(
                    NumericPreferenceFactor(
                        rule.name,
                        rule.extractor,
                        rule.min_value,
                        rule.max_value,
                        rule.weight,
                        rule.minimize
                    )
                )
            elif rule.data_type == "SELECTION":
                preferences.append(
                    SelectionPreferenceFactor(
                        rule.name,
                        rule.extractor,
                        rule.weight
                    )
                )

degree_level_constraint = UserRule( # hard-coded: need to be the right degree level
    name="degree_level_constraint",
    mode="HARD",    
    extractor=lambda s, p: (s.degree_level_factor, p.degree_level),
    operator=operator.eq,
    weight=1.0,
    data_type="SELECTION"
)

schedule_factor = UserRule(
    "schedule_type_factor",
    mode="SOFT",
    extractor=lambda s, p: (s.schedule_type_factor, p.schedule_type),
    operator=operator.eq,
    weight=1.0,
    data_type="SELECTION"
)

distance_factor = UserRule( # in miles
    name="distance_factor",
    mode="SOFT",
    extractor=lambda s, p: s.distance_to(p.program_profile.school.location),
    min_value=0,
    max_value=500,
    weight=1.0,
    minimize=True
)
tuition_factor = UserRule( # in USD
    name="tuition_factor",
    mode="SOFT",
    extractor=lambda s, p: p.tuition,
    min_value=0,
    max_value=60000, # replace this with a real max value from Dr. E's knowledge
    weight=2.0,
    minimize=True
)
tuition_constraint = UserRule( # in USD
    name="tuition_factor",
    mode="HARD",
    extractor=lambda s, p: (s.max_tuition, p.tuition),
    operator=operator.le
)
acceptance_rate_factor = UserRule(
    name="acceptance_rate_factor",
    mode="SOFT",
    extractor=lambda s, p: p.acceptance_rate,
    min_value=0.0,
    max_value=1.0,
    weight=0.5,
    minimize=False
)

dorm_requirement_factor = UserRule(
    name="dorm_requirement_factor",
    mode="SOFT",
    extractor=lambda s, p: (s.dorm_requirement_factor, p.dorm_requirement),
    operator=operator.eq,
    weight=1.0,
    data_type="SELECTION"
)

dorm_availability_factor = UserRule(
    name="dorm_availability_factor",
    mode="SOFT",
    extractor=lambda s, p: (s.dorm_availability_factor, p.dorm_availability),
    operator=operator.eq,
    weight=1.0,
    data_type="SELECTION"
)

factors = [distance_factor, tuition_factor, acceptance_rate_factor, degree_level_constraint, schedule_factor, tuition_constraint, acceptance_rate_factor, dorm_requirement_factor, dorm_availability_factor]

def score_program(self, request: HttpRequest, program: Program):
    if request.user.account_type == CustomUser.AccountType.STUDENT:
        student = request.user.student
    total_score = 0
    for factor in factors:
        total_score += factor.score(student, program)

    if total_score > heapq.nlargest:
        heapq.heappush(top_ten, total_score)
        heapq.heappop(top_ten, heapq.nsmallest)


def get_ranked_programs(self, request):
    ranked_programs = list()
    for i in len(heapq):
        ranked_programs.append(heapq.nlargest)
    return ranked_programs