from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from urllib.error import HTTPError
from .forms import HostCreationForm, ExtendedUserCreationForm, WorkerCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request, user_type):
    """A view that manages the registration form"""
    if user_type == 'host':
        profile_form = HostCreationForm()
        post_paramater = 'host'
    elif user_type == 'worker':
        profile_form = WorkerCreationForm()
        post_paramater = 'worker'
    form = ExtendedUserCreationForm()
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST)
        if user_type == 'host':  
            profile_form = HostCreationForm(request.POST)
        elif user_type == 'worker':
            profile_form = WorkerCreationForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponse("registered!")
        else:
            print(profile_form.errors.values())
            return HttpResponse(user_form.errors.values())
    print(profile_form)
    return render(request, 'accounts/register.html', {'form': form, 'profile_form': profile_form, 'post_paramater': post_paramater})


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        print('hellothen')
        user_form = AuthenticationForm(request.POST)
        #if user_form.is_valid():
        print(request.POST)
        user = authenticate(request, username=request.POST['your_name'], password=request.POST['your_pass'])
        if user:
            auth_login(request, user)
            return HttpResponse("logged in")
        else:
            return HttpResponse("login details incorrect")
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return HttpResponse('logged out')
    #return redirect(request, 'accounts/login.html')



