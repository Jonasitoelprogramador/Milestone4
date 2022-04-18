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
from django.contrib.auth.decorators import user_passes_test
from users.views import host_worker_exist


def logged_in_check(user):
    if user.is_authenticated:
        return False
    else:
        return True


@user_passes_test(logged_in_check, login_url="/")
# Create your views here.
def signup(request):
    form1 = ExtendedUserCreationForm()
    form2 = RoleForm()
    # if method is POST, bind inputted data to user and role forms respectively
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST)
        Role_form = RoleForm(request.POST)
        # validate and authenticate both forms
        if user_form.is_valid() and Role_form.is_valid():
            user = user_form.save()
            form = Role_form.save(commit=False)
            form.user = user
            # if both valid, save forms
            form.save()
            authenticated_user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
            if authenticated_user:
                # if correctly authenticated, login
                auth_login(request, authenticated_user)
            return redirect(profile)
        else:
            return render(request, 'accounts/sign_up.html', {"form1": form1, "form2": form2, "errors": user_form.errors.values()})
    return render(request, 'accounts/sign_up.html', {"form1": form1, "form2": form2})


@user_passes_test(logged_in_check, login_url="/")
def login(request):
    """A view that manages the login form"""
    authentication_form = AuthenticationForm()
    # if request type is POST
    if request.method == 'POST':
        user_form = AuthenticationForm(request.POST)
        # authenticate user
        authenticated_user = authenticate(request, username=request.POST['your_name'], password=request.POST['your_pass'])
        if authenticated_user:
            #if properly authenticated, login user
            auth_login(request, authenticated_user)
            # redirect to profile page
            if str(authenticated_user.role) == "host":
                return redirect(profile)
            elif str(authenticated_user.role) == "worker":
                return redirect(profile)
        else:
            # if authenticate not valid, show errors
            return render(request, 'accounts/login.html', {'form': authentication_form, 'errors': "credentials incorrect"})
    return render(request, 'accounts/login.html', {'form': authentication_form})


def logout(request):
    # logout and redirect to login page
    auth_logout(request)
    return redirect(login)




