from django.shortcuts import render
from django.forms import modelformset_factory
from django.shortcuts import render
from django.views import generic
from .forms import InternForm
from .forms import CommentForm
from .forms import EditFrom
from .models import Intern
from positions.models import Position
from .models import Comments
from django.http import HttpResponseRedirect
from pprint import pprint
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from django.contrib import messages


class RegisterView(generic.CreateView):
    template_name = 'formularStazista.html'
    model = Intern
    form_class = InternForm
    success_url = '/diky/'

    def form_valid(self, form):
        # print('PASSES VALIDATION')
        newintern = form.save(commit=False)
        # pprint(vars(newintern))
        newintern.assigned_coordinator = User.objects.last()
        newintern.save()
        return super(RegisterView, self).form_valid(form)


class InternsTable(generic.CreateView):
    """Login view as home page."""
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
    print('-----------------------------------------')
    if not request.user.is_authenticated():
        raise Http404

    form = EditFrom(request.POST)
    pprint(request.POST)
    form.full_clean()
    # print('-----------------------------VALID---------------')
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
    print("---------------------------------------")
    newIntern.assigned_coordinator = User.objects.get(username=request.POST['assigned_coordinator'])
    if request.POST['position'] != '':
        newIntern.position = Position.objects.get(position_name=request.POST['position']).__str__()
    newIntern.save()
    messages.success(request, 'Profile was UPDATED!')
    return redirect('/staziste/')

# else:
# messages.error(request, 'Profile was not updated!')
# return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
