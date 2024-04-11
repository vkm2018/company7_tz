from django.contrib.auth.forms import AuthenticationForm
from django import forms
from apps.account.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    class Meta:
        model = User
        fields = ('username', 'password')

