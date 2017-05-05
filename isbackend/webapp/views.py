from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.utils import timezone

#from .models import News #co to dela?
#from general.models import DateOptions, AboutWidget


class viewLogin(generic.TemplateView):
    """Login view as home page."""

    template_name = 'prihlaseni.html'

class viewIntern(generic.TemplateView):
    """Login view as home page."""

    template_name = 'staziste.html'



