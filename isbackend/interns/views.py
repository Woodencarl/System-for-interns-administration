from django.shortcuts import render
from django.forms import modelformset_factory
from django.shortcuts import render
from django.views import generic
from .forms import InternForm
from .forms import CommentForm
from .models import Intern
from positions.models import Position
from .models import Comments
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from pprint import pprint
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404


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
        newcomment.intern = get_object_or_404(pk=intern_id)
        newcomment.author = request.user
        newcomment.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def edit_profile(request, intern_id):
    intern = get_object_or_404(Intern, pk=intern_id)
    return render(request, 'editovatProfilStazisty.html',
                  {'intern': intern, 'users': User.objects.all(), 'positions': Position.objects.filter(is_active=True)})


def save_edit_profile(request, intern_id):
    if not request.user.is_authenticated():
        raise Http404

    form = CommentForm(request.POST)
    if form.is_valid():
        print('-------------------------------------from user ID')
        newcomment = form.save(commit=False)
        newcomment.intern = get_object_or_404(pk=intern_id)
        newcomment.author = request.user
        newcomment.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



