from django.shortcuts import render
from django.views import generic
from .models import Subscriber


class viewSubscribers(generic.TemplateView):
    """Login view as home page."""

    template_name = 'odberatele.html'
    model = Subscriber
    fields = '__all__'
    page_name = 'Odběratelé'

    def get_context_data(self, **kwargs):
        """Feed the template with all required DB data to display."""
        # get the context object
        context = super(viewSubscribers, self).get_context_data(**kwargs)
        # pprint(Intern.objects.filter(active=True))
        context['subscribers_list'] = Subscriber.objects.all()
        context['page_name'] = 'Odběratelé'
        return context


def delete_sub(request, sub_id):
    pass


class viewSubscribersForm(generic.TemplateView):
    """Login view as home page."""

    template_name = 'formularNovinky.html'
