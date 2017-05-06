from django.shortcuts import render


from django.views import generic
# Create your views here.
class viewSubscribers(generic.TemplateView):
    """Login view as home page."""

    template_name = 'odberatele.html'

class viewSubscribersForm(generic.TemplateView):
    """Login view as home page."""

    template_name = 'formularNovinky.html'
