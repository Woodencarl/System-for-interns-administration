from django.shortcuts import render
from django.views import generic
from .forms import InternForm
from .forms import CommentForm
from .forms import EditFrom
from .models import Intern
from positions.models import Position
from isbackend import settings
from .models import Comments
from django.http import HttpResponseRedirect
from pprint import pprint
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template


class RegisterView(generic.CreateView):
    """View making form for registration to internship program"""
    template_name = 'formularStazista.html'
    model = Intern
    form_class = InternForm
    success_url = '/diky/'

    def form_valid(self, form):
        form.full_clean()
        newintern = form.save(commit=False)
        newintern.assigned_coordinator = User.objects.last()
        newintern.save()
        # redy for improvement by sending emails in html format
        # msg_plain = render_to_string(get_template('mails/registracni_email.txt'), {'intern': newintern})
        # msg_html = render_to_string(get_template('mails/registracni_email.html'), {'intern': newintern})
        #
        # send_mail('Registrace probehla uspesne',
        #           msg_plain,
        #           'interns.system@seznam.cz',
        #           [newintern.e_mail], fail_silently=True, html_message=msg_html)

        body = 'Ahoj, děkujeme za tvoji registraci.Za pár dní se ti ozveme.' \
               'Pokud chceš kdykoliv smazat své osobní údaje z naší databáze, zde je permanentní odkaz: ' + \
               settings.ALLOWED_HOSTS[0] + \
               '/staziste/smazat/' + newintern.id.__str__()
        send_mail('Registrace probehla uspesne',
                  body,
                  settings.EMAIL_HOST_USER,
                  [newintern.e_mail], fail_silently=True)

        body2 = 'Ahoj, prave se registroval novy zajemce o staz.' \
                'Jméno: ' + newintern.first_name + newintern.last_name + \
                'Email: ' + newintern.e_mail + \
                'Telefon: ' + newintern.phone

        send_mail('Novy registrovany',
                  body2,
                  settings.EMAIL_HOST_USER,
                  [newintern.assigned_coordinator.email], fail_silently=True)

        return super(RegisterView, self).form_valid(form)


class InternsTable(generic.CreateView):
    """Interns table view to serve data for page."""
    template_name = 'staziste.html'
    model = Intern
    fields = '__all__'
    page_name = 'Stážisté'

    def get_context_data(self, **kwargs):
        """Feed the template with all required DB data to display."""
        # get the context object
        context = super(InternsTable, self).get_context_data(**kwargs)
        # pprint(Intern.objects.filter(active=True))
        context['interns_list'] = Intern.objects.filter(active=True)
        context['page_name'] = 'Stážisté'
        return context


class ProfileView(generic.FormView):
    template_name = 'profilStazisty.html'
    model = Comments
    form_class = CommentForm
    success_url = ''

    def get_context_data(self, **kwargs):
        """Feed the template with all required DB data to display."""
        context = super(ProfileView, self).get_context_data(**kwargs)
        intern_id = self.kwargs['intern_id']
        context['interns_list'] = Intern.objects.filter(pk=intern_id)
        context['comments'] = Comments.objects.filter(intern=intern_id).order_by('-create_datetime')
        context['page_name'] = 'Stážisté'
        return context


def create_comment(request, intern_id):
    if not request.user.is_authenticated():
        raise Http404

    form = CommentForm(request.POST)
    if form.is_valid():
        print('-------------------------------------from user ID')
        newcomment = form.save(commit=False)
        newcomment.intern = get_object_or_404(Intern, pk=intern_id)
        newcomment.author = request.user
        newcomment.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def edit_profile(request, intern_id):
    intern = get_object_or_404(Intern, pk=intern_id)
    page_name = "Edit " + intern.first_name + " " + intern.last_name
    return render(request, 'editovatProfilStazisty.html',
                  {'intern': intern, 'users': User.objects.all(),
                   'positions': Position.objects.filter(is_active=True),
                   'page_name': page_name})


def save_edit_profile(request, intern_id):
    if not request.user.is_authenticated():
        raise Http404

    form = EditFrom(request.POST)

    form.full_clean()
    newIntern = get_object_or_404(Intern, pk=intern_id)
    newIntern.first_name = request.POST['first_name']
    newIntern.last_name = request.POST['last_name']
    newIntern.e_mail = request.POST['e_mail']
    newIntern.phone = request.POST['phone']
    newIntern.school = request.POST['school']
    newIntern.faculty = request.POST['faculty']
    newIntern.year = request.POST['year']
    newIntern.field = request.POST['field']
    newIntern.mentor = request.POST['mentor']
    newIntern.division = request.POST['division']
    if request.POST['date_of_birth'] != '':
        newIntern.date_of_birth = request.POST['date_of_birth']
    if request.POST['first_interview_date'] != '':
        newIntern.first_interview_date = request.POST['first_interview_date']
    if request.POST['second_interview_date'] != '':
        newIntern.second_interview_date = request.POST['second_interview_date']
    if request.POST['contract_till'] != '':
        newIntern.contract_till = request.POST['contract_till']
    newIntern.status = request.POST['status']

    newIntern.assigned_coordinator = User.objects.get(username=request.POST['assigned_coordinator'])
    if newIntern.position is not None:
        setattr(Position.objects.get(position_name=newIntern.position), 'is_active', True)
    if request.POST['position'] != '':
        setattr(Position.objects.get(position_name=request.POST['position']), 'is_active', False)
        Position.objects.get(position_name=request.POST['position']).save()
        newIntern.position = Position.objects.get(position_name=request.POST['position']).__str__()
    else:
        newIntern.position = None
    newIntern.save()
    messages.success(request, 'Profile was UPDATED!')
    return redirect('/staziste/')


def close_profile(request, intern_id):
    intern = get_object_or_404(Intern, pk=intern_id)
    setattr(intern, 'active', False)
    intern.save()
    return redirect('/staziste/')


def erase_profile(request, intern_id):
    """Funcion based view for erasing intern from database"""
    Intern.objects.filter(pk=intern_id).delete()
    # if request.user.is_authenticated(): # is_auth. bohuzel pri neprihlaseni presmeruje na prihlasovaci stranku
    #     return redirect('/staziste/')
    # else:
    return redirect('/smazany/')


def send_to_intern(request, intern_id):
    recieverintern = get_object_or_404(Intern, pk=intern_id)
    body = 'Odkaz pro smazání.' \
           'Pokud chceš kdykoliv smazat své osobní údaje z naší databáze, zde je permanentní odkaz: ' + \
           settings.ALLOWED_HOSTS[0] + \
           '/staziste/smazat/' + recieverintern.id.__str__()

    send_mail('Registrace probehla uspesne',
              body,
              settings.EMAIL_HOST_USER,
              [recieverintern.e_mail], fail_silently=True)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))