from django.db import models

# Create your models here.


class ScoringManager:
    success_rate = models.FloatField(default=0.0)
    past_scores = models.JSONField(default=dict)

    