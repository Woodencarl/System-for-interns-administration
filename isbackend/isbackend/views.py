from django.views import generic


class ThanksView(generic.TemplateView):

    template_name = 'diky.html'


class DeleteView(generic.TemplateView):

    template_name = 'smazany.html'


class AgreeView(generic.TemplateView):

    template_name = 'souhlas.html'
