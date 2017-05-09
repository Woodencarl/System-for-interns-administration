from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    pass
    # class Meta:
    #     model = User
    #     fields = ('username', 'password')
