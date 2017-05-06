from django.shortcuts import render


from django.views import generic
# Create your views here.
class viewPositions(generic.TemplateView):
    """Login view as home page."""

    template_name = 'pozice.html'

class viewPositionsForm(generic.TemplateView):
    """Login view as home page."""

    template_name = 'formularPozice.html'

