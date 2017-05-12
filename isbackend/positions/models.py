from django.db import models


class Position(models.Model):
    is_active = models.BooleanField(default=True)
    mentor_name = models.CharField('Mentor', max_length=50)
    division = models.CharField('Divize', max_length=100)
    pros_of_mentor = models.CharField('Mentorovy přednosti', max_length=2000)
    position_name = models.CharField('Jméno pozice', max_length=50)
    position_description = models.CharField('Popis pozice', max_length=2000)
    project = models.CharField('Projekt', max_length=1000)
    benefit_for_intern = models.CharField('Výhody pro stážistu', max_length=1000)
    requirements = models.CharField('Požadavky', max_length=1000)
    notes = models.CharField('Poznámky', max_length=1000)
    registration_date = models.DateField('Datum registrace',  auto_now_add=True)

    def __str__(self):
        return self.position_name
