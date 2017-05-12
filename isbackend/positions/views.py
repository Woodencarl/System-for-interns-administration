from django.shortcuts import render
from .models import Position
from django.shortcuts import get_object_or_404, redirect
from django.views import generic


class viewPositions(generic.TemplateView):
    """Login view as home page."""

    template_name = 'pozice.html'

    def get_context_data(self, **kwargs):
        """Feed the template with all required DB data to display."""
        # get the context object
        context = super(viewPositions, self).get_context_data(**kwargs)
        context['position_list'] = Position.objects.filter(is_active=True)
        context['page_name'] = 'Pozice'
        return context


class viewDetailPosition(generic.TemplateView):
    template_name = 'detailPozice.html'

    def get_context_data(self, **kwargs):
        """Feed the template with all required DB data to display."""
        context = super(viewDetailPosition, self).get_context_data(**kwargs)
        position_id = self.kwargs['position_id']
        context['position_list'] = Position.objects.filter(pk=position_id)
        context['page_name'] = 'Detail pozice'
        return context


def close_position(request, position_id):
    position = get_object_or_404(Position, pk=position_id)
    setattr(position, 'is_active', False)
    position.save()
    return redirect('/pozice/')


class ViewPositionsForm(generic.TemplateView):
    """Login view as home page."""
    template_name = 'formularPozice.html'
    success_url = '/diky/'
