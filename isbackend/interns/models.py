from django.db import models
from positions.models import Position
from django.contrib.auth.models import User

import os


class Intern(models.Model):
    LEARNED_FORM_OPTIONS = (
        ('K', 'Od kamaráda'),
        ('V', 'Z veletrhu'),
        ('F', 'Z Facebooku'),
        ('S', 'Ze školy'),
        ('U', 'Od učitele'),
        ('R', 'Od rodiče'),
        ('A', 'Sám jsem si našel'),
        ('J', 'Jinak')
    )

    first_name = models.CharField('Jméno', max_length=30)
    last_name = models.CharField('Příjmení', max_length=30)
    date_of_birth = models.DateField('Datum narození')
    e_mail = models.EmailField('E-mail')
    phone = models.CharField('Telefon', max_length=20)
    school = models.CharField('Škola', max_length=50)
    faculty = models.CharField('Fakulta', max_length=50)
    year = models.CharField('ročník', max_length=20)
    field = models.CharField('Zaměření', max_length=50)
    interests = models.ManyToManyField(Position, verbose_name='Zájem')
    learned_from = models.CharField('Dozvěděl se od', max_length=1, choices=LEARNED_FORM_OPTIONS)
    resume = models.FileField('Životopis', upload_to='resumes/%Y/%m')
    cover_letter = models.FileField('Motivační dopis', upload_to='cover_letters/%Y/%m')
    registration_date = models.DateField('Datum registrace', auto_now_add=True)
    first_interview_date = models.DateField('Datum prvního pohovoru', blank=True, null=True)
    second_interview_date = models.DateField('Datum druhého pohovoru', blank=True, null=True)
    wanted_boarding_date = models.DateField('Datum chtěného nástupu', auto_now_add=True)
    contract_till = models.DateField('Reálné datum nástupu', blank=True, null=True)
    mentor = models.CharField('Mentor', max_length=50, blank=True, null=True, default='Bez mentora')
    division = models.CharField('Divize', max_length=50, blank=True, null=True, default='Bez divize')
    position = models.CharField('Pozice', max_length=50, blank=True, null=True, default='Bez pozice')
    assigned_coordinator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    status = models.CharField('Status', max_length=200, blank=True, default='Novy')
    active = models.BooleanField('Aktivní', default=True)


class Comments(models.Model):
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE)
    create_datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)  # later username when login app will work - name of logged person
    comment = models.CharField(max_length=10000)
