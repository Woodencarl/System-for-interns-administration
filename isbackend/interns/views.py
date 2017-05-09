from django.shortcuts import render
from django.forms import modelformset_factory
from django.shortcuts import render
from django.views import generic
from .forms import InternForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login



def manage_form_intern(request):
    if request.method == 'POST':
        form = InternForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # do something.
    else:
        form = InternForm()
    return render(request, 'formularStazista.html', {'form': form})


class viewIntern(generic.TemplateView):
    """Login view as home page."""

    template_name = 'staziste.html'
