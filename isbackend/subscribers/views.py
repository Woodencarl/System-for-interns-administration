from django.shortcuts import render
from django.views import generic
from .models import Subscriber
from django.shortcuts import redirect
from .forms import NewsFrom
from .models import INTEREST_LIST
from django.contrib import messages


class ViewSubscribers(generic.TemplateView):
    """View for subscribers table"""
    template_name = 'odberatele.html'
    model = Subscriber
    fields = ('first_name', 'last_name', 'e_mail', 'phone', 'school', 'year',
              'obligation', 'interests')
    page_name = 'Odběratelé'

    def get_context_data(self, **kwargs):
        """Feed the template with all required DB data to display."""
        context = super(ViewSubscribers, self).get_context_data(**kwargs)
        context['subscribers_list'] = Subscriber.objects.all()
        context['page_name'] = 'Odběratelé'
        return context


def delete_sub(request, sub_id):
    Subscriber.objects.filter(pk=sub_id).delete()
    if request.user.is_authenticated():
        return redirect('/odberatele/')
    else:
        return redirect('/smazany/')


class ViewSubscribersForm(generic.CreateView):
    """View that serves subscriber form"""
    form_class = NewsFrom
    template_name = 'formularNovinky.html'
    success_url = '/diky/'

    def form_valid(self, form):
        form.full_clean()
        newsub = form.save(commit=False)

        newsub.interests += ", " + self.request.POST['other']
        print('-------------------------------------')
        newsub.save()
        return super(ViewSubscribersForm, self).form_valid(form)

    def form_invalid(self, form):
        return super(ViewSubscribersForm, self).form_invalid(form)
