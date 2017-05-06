from django.db import models


class Intern(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    male = models.BooleanField()
    date_of_birth = models.DateField()
    e_mail = models.EmailField()
    phone = models.CharField(max_length=20)
    school = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    field = models.CharField(max_length=50)
    interests = models.CharField(max_length=200)
    learned_from = models.CharField(max_length=100)
    resume = models.FileField()
    cover_letter = models.FileField()
    registration_date = models.DateField(auto_now_add=True)
    first_interview_date = models.DateField()
    second_interview_date = models.DateField()
    wanted_boarding_date = models.DateField()
    real_boarding_date = models.DateField()
    mentor = models.CharField(max_length=50)
    division = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    assigned_coordinator = models.CharField(max_length=100)
    status = models.CharField(max_length=200)


class Comments(models.Model):
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=50)
    comment = models.CharField(max_length=10000)