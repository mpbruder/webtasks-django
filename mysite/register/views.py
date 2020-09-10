from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render

from .forms import EditProfileForm, RegisterForm


# Create your views here.
def register(response):
    form = RegisterForm(response.POST or None)
    if form.is_valid():
        user = form.save()
        user = authenticate(
            username=user.username,
            password=form.cleaned_data['password1']
            # 'user.password' é uma senha criptografada que vai para o BD.
        )
        # Colocar o usuário na sessão
        login(response, user)
        messages.success(response, 'Nova conta cadastrada!')
        return redirect("register:dashboard")

    template_name = 'register/register.html'
    context = {
        'form': form,
    }
    return render(response, template_name, context)


@login_required
def dashboard(response):
    template_name = 'register/dashboard.html'
    context = {}
    return render(response, template_name, context)


class myLoginView(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'
    success_url = 'main:home'
    success_message = 'Login realizado'


@login_required
def change_password(response):
    if response.method == 'POST':
        form = PasswordChangeForm(response.user, response.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(response, user)  # Important!
            messages.success(response, 'Sua senha foi alterada')
            return redirect('register:dashboard')
        else:
            messages.error(response, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(response.user)
    template_name = 'register/change_password.html'
    context = {
        'form': form,
    }
    return render(response, template_name, context)


@login_required
def edit_profile(response):
    if response.method == 'POST':
        form = EditProfileForm(response.POST, instance=response.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(response, user)  # Important!
            messages.success(response, 'Seus dados foram alterados')
            return redirect('register:dashboard')
        else:
            messages.error(response, 'Please correct the error below.')
    else:
        form = EditProfileForm(instance=response.user)
    template_name = 'register/edit_profile.html'
    context = {
        'form': form,
    }
    return render(response, template_name, context)
