from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.utils import timezone


#from general.models import DateOptions, AboutWidget


class viewLogin(generic.TemplateView):
    """Login view as home page."""

    template_name = 'prihlaseni.html'




