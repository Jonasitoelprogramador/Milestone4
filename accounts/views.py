from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from urllib.error import HTTPError

# Create your views here.
def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse("registered!")
        else:
            print(user_form.errors.values())
            return HttpResponse(user_form.errors.values())
    form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            print(request.POST)
            user = authenticate(request, username=request.POST['username_or_email'], password=request.POST['password'])

            if user:
                auth_login(request, user)
                return HttpResponse("logged in")
            else:
                return HttpResponse("login details incorrect")
    form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'accounts/profile.html')
    

def logout(request):
    auth_logout(request)
    return HttpResponse('logged out')
    #return redirect(request, 'accounts/login.html')
