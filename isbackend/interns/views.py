from django.shortcuts import render
from django.forms import modelformset_factory
from django.shortcuts import render
from django.views import generic
from .forms import InternForm
from .models import Intern
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from pprint import pprint
from django.contrib.auth.models import User


class RegisterView(generic.CreateView):
    template_name = 'formularStazista.html'
    model = Intern
    form_class = InternForm
    success_url = '/diky/'
    print('-------------LETS LIST ALL INTERNS-----------------')

    # pprint(Intern.objects.filter(
    #         active=True))
    # for intern in Intern.objects:
    #     print(intern.first_name)

    def form_valid(self, form):
        print('PASSES VALIDATION')
        newintern = form.save(commit=False)
        newintern.status = 'Novy'
        pprint(vars(newintern))
        newintern.save()
        # co se ulozi do newIntern? musim definovat vsechny sloupce?
        # co kdyz frontend znehodnoti form?
        return super(RegisterView, self).form_valid(form)


class viewIntern(generic.CreateView):
    """Login view as home page."""
    template_name = 'staziste.html'
    model = Intern
    fields = '__all__'

    def get_context_data(self, **kwargs):
        """Feed the template with all required DB data to display."""
        # get the context object
        context = super(viewIntern, self).get_context_data(**kwargs)
        pprint(Intern.objects.filter(active=True))
        context['interns_list'] = [(Intern.objects.filter(
            active=True))]

        return context


class ThanksView(generic.TemplateView):
    template_name = 'diky.html'
