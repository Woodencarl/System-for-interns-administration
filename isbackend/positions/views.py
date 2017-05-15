from django.shortcuts import render
from .models import Position
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .forms import PosForm
from isbackend import settings


class ViewPositions(generic.TemplateView):
    """Login view as home page."""

    template_name = 'pozice.html'

    def get_context_data(self, **kwargs):
        """Feed the template with all required DB data to display."""
        # get the context object
        context = super(ViewPositions, self).get_context_data(**kwargs)
        context['position_list'] = Position.objects.filter(is_active=True)
        context['page_name'] = 'Pozice'
        return context


class ViewDetailPosition(generic.TemplateView):
    template_name = 'detailPozice.html'

    def get_context_data(self, **kwargs):
        """Feed the template with all required DB data to display."""
        context = super(ViewDetailPosition, self).get_context_data(**kwargs)
        position_id = self.kwargs['position_id']
        context['position_list'] = Position.objects.filter(pk=position_id)
        context['page_name'] = 'Detail pozice'
        return context


def close_position(request, position_id):
    position = get_object_or_404(Position, pk=position_id)
    setattr(position, 'is_active', False)
    position.save()
    return redirect('/pozice/')


class ViewPositionsForm(generic.CreateView):
    """Login view as home page."""
    template_name = 'formularPozice.html'
    success_url = '/diky/'
    form_class = PosForm

    def form_valid(self, form):
        form.full_clean()
        newpos = form.save(commit=False)
        newpos.save()
        body = 'Ahoj, prave se nekdo vypsal pozici na staz.' \
               'Pozice: ' + newpos.position_name + \
                'Mentor: ' + newpos.mentor_name
        send_mail('Novy registrovany',
                  body,
                  settings.EMAIL_HOST_USER,
                  [User.objects.last()], fail_silently=True)

        return super(ViewPositionsForm, self).form_valid(form)