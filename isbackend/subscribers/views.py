import csv
from django.views import generic
from .models import Subscriber
from django.shortcuts import redirect
from .forms import NewsFrom
from django.core.mail import send_mail
from django.http import HttpResponse
from isbackend import settings
from django.utils.encoding import smart_str
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
    """Funcion based view for erasing subscriber from database"""
    Subscriber.objects.filter(pk=sub_id).delete()
    # if request.user.is_authenticated(): # is_auth... kdyz neprojde tak presmeruje na prihlaseni
    #     return redirect('/odberatele/')
    # else:
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
        newsub.save()
        # print('-------------------------------------')
        body = 'Ahoj, děkujeme za tvoji registraci.Za pár dní se ti ozveme.' \
               'Pokud se chceš odhlásit z odběru, zde je permanentní odkaz: ' + settings.ALLOWED_HOSTS[0] + \
               '/odberatele/smazat/' + newsub.sub_id.__str__()
        send_mail('Prihlaseni k odberu', body,
                  settings.EMAIL_HOST_USER,
                  [newsub.e_mail], fail_silently=True)
        return super(ViewSubscribersForm, self).form_valid(form)

    def form_invalid(self, form):
        return super(ViewSubscribersForm, self).form_invalid(form)


def download_csv(request):
    queryset = Subscriber.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=subscribers.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"e_mail"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.e_mail),
        ])

    print('-----------------------------------------------------')
    return response
