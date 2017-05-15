from django.db import models
import uuid
from uuid import uuid4


OBLIGATION_LIST = (
        ('Stáž', 'Stáž'),
        ('Částečný úvazek', 'Částečný úvazek'),
        ('Plný úvazek', 'Plný úvazek'),
    )

INTEREST_LIST = (
    ('Design', 'Design'),
    ('Umělá inteligence', 'Umělá inteligence'),
    ('Obchod', 'Obchod'),
    ('Management', 'Management'),
    ('Systémy', 'Systémy'),
)


class Subscriber(models.Model):
    sub_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    e_mail = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    school = models.CharField(max_length=50, null=True, blank=True)
    year = models.CharField(max_length=20, null=True, blank=True)
    obligation = models.CharField(max_length=100, null=True, blank=True)
    interests = models.CharField(max_length=300, null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)

