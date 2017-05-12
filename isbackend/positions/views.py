from django.shortcuts import render


from django.views import generic
# Create your views here.
class viewPositions(generic.TemplateView):
    """Login view as home page."""

    template_name = 'pozice.html'
    def get_context_data(self, **kwargs):
        """Feed the template with all required DB data to display."""
        # get the context object
        context = super(InternsTable, self).get_context_data(**kwargs)
        context['page_name'] = 'Stážisté'
        return context

class viewPositionsForm(generic.TemplateView):
    """Login view as home page."""

    template_name = 'formularPozice.html'

