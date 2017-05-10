from django.shortcuts import render
from django.forms import modelformset_factory
from django.shortcuts import render
from django.views import generic
from .forms import InternForm
from .models import Intern
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login


def manage_form_intern(request):
    if request.method == 'POST':
        form = InternForm(request.POST, request.FILES)

        if form.is_valid():
            newIntern = form
            newIntern = Intern(resume=request.FILES['resume'], cover_letter=request.FILES['cover_letter'])
            print('form is valid')
            newIntern.save()
            #co se ulozi do newIntern? musim definovat vsechny sloupce?
            #co kdyz frontend znehodnoti form?
            return HttpResponseRedirect('/thanks/')
        else:
            print('NOT VALID')

            # do something.
    else:
        form = InternForm()
    return render(request, 'formularStazista.html', {'form': form})


class viewIntern(generic.TemplateView):
    """Login view as home page."""

    template_name = 'staziste.html'


class ThanksView(generic.TemplateView):

    template_name = 'diky.html'
