from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm


#from general.models import DateOptions, AboutWidget


def viewLogin(request):
    """Login view as home page."""

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('staziste/')
        else:
            print('form is not valid')
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'prihlaseni.html', {'form': form})



