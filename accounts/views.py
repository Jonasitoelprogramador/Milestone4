from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserLoginForm

# Create your views here.
def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse("beery butt men")
        else:
            return HttpResponse("unable to log you in at this time!")
    form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = authenticate(request.POST['username_or_email'],
                                    password=request.POST['password'])

            if user:
                login(request, user)
                return HttpResponse("logged in")
            else:
                return HttpResponse("login details incorrect")
    form = UserLoginForm()
    return render(request, 'accounts/register.html', {'form': form})