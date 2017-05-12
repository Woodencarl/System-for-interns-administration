from django.db import models


class Subscriber(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    e_mail = models.EmailField()
    phone = models.CharField(max_length=20, null=True)
    school = models.CharField(max_length=50, null=True)
    year = models.CharField(max_length=20, null=True)
    obligation = models.CharField(max_length=80, null=True)
    interests = models.CharField(max_length=300, null=True)
    registration_date = models.DateField(auto_now_add=True)

