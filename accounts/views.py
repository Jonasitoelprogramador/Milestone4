from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from urllib.error import HTTPError
from .forms import ExtendedUserCreationForm, RoleForm
from django.contrib.auth.forms import AuthenticationForm
from users.views import all_offerings, all_workers, profile
from django.urls import reverse


# Create your views here.
def signup(request):
    form1 = ExtendedUserCreationForm()
    form2 = RoleForm()
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST)
        Role_form = RoleForm(request.POST)
        if user_form.is_valid() and Role_form.is_valid():
            user = user_form.save()
            form = Role_form.save(commit=False)
            form.user = user
            form.save()
            authenticated_user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
            if authenticated_user:
                auth_login(request, authenticated_user)
            return redirect(profile)
        else:
            return render(request, 'accounts/sign_up.html', {"form1": form1, "form2": form2, "errors": user_form.errors.values()})
    return render(request, 'accounts/sign_up.html', {"form1": form1, "form2": form2})


def login(request):
    """A view that manages the login form"""
    authentication_form = AuthenticationForm()
    if request.method == 'POST':
        print(request.POST)
        user_form = AuthenticationForm(request.POST)
        authenticated_user = authenticate(request, username=request.POST['your_name'], password=request.POST['your_pass'])
        if authenticated_user:
            auth_login(request, authenticated_user)
            if str(authenticated_user.role) == "host":
                return redirect(profile)
            elif str(authenticated_user.role) == "worker":
                return redirect(profile)
        else:
            return render(request, 'accounts/login.html', {'form': authentication_form, 'errors': "credentials incorrect"})
    return render(request, 'accounts/login.html', {'form': authentication_form})


def logout(request):
    auth_logout(request)
    return redirect(login)




