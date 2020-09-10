from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='E-mail')
    first_name = forms.CharField(label='Primeiro nome', max_length=100, required=False)
    last_name = forms.CharField(label='Último nome', max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2',]


class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='E-mail')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',]