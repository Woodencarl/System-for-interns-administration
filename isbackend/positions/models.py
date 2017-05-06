from django.db import models

class Position(models.Model):
    mentor_name = models.CharField(max_length=50)
    division = models.CharField(max_length=100)
    pros_of_mentor = models.CharField(max_length=2000)
    position_name = models.CharField(max_length=50)
    position_description = models.CharField(max_length=2000)
    project = models.CharField(max_length=1000)
    benefit_for_intern = models.CharField(max_length=1000)
    requirements = models.CharField(max_length=1000)
    notes = models.CharField(max_length=1000)
    registration_date = models.DateField(auto_now_add=True)
