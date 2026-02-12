from django.db import models


class DegreeLevel(models.IntegerChoices):
    NONE = 0
    PRACTICAL_NURSING = 1
    ASN = 2
    BSN = 3
    BSN_PRELIC = 4
    GRAD_CERT = 5
    MSN = 6
    MSN_PRELIC = 7
    DNP = 8
    PHD = 9

class ProgramFormat(models.IntegerChoices):
    NONE = 0
    TRADITIONAL = 1
    ACCELERATED = 2
    BRIDGE = 3
    POST_BACC = 4
    N_A = 5

class DegreeSpecialty(models.IntegerChoices):
    NONE = 0
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