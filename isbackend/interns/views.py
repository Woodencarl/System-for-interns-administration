from django.shortcuts import render

from django.views import generic
# Create your views here.
class viewIntern(generic.TemplateView):
    """Login view as home page."""

    template_name = 'staziste.html'

class viewInternForm(generic.TemplateView):
    """Login view as home page."""

    template_name = 'formularStazista.html'
