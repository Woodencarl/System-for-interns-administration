from django.db import models


class Subscriber(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    e_mail = models.EmailField()
    phone = models.CharField(max_length=20)
    school = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    obligation = models.CharField(max_length=80)
    interests = models.CharField(max_length=200)
    registration_date = models.DateField(auto_now_add=True)

