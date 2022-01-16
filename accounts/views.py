from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from urllib.error import HTTPError
from .forms import ExtendedUserCreationForm, TypeForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(request):
    form1 = ExtendedUserCreationForm()
    form2 = TypeForm()
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST)
        type_form = TypeForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
        if type_form.is_valid():
            form = type_form.save(commit=False)
            form.user = user
            form.save()
            return HttpResponse("registered!")
        else:
            return HttpResponse(user_form.errors.values())
    return render(request, 'accounts/sign_up.html', {"form1": form1, "form2": form2})


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
            return HttpResponse("logged in baby!")
        else:
            return HttpResponse("login details incorrect")
    authentication_form = AuthenticationForm()
    account_type_form = TypeForm()
    return render(request, 'accounts/login.html', {'form': authentication_form, 'form2': account_type_form})


def logout(request):
    auth_logout(request)
    return HttpResponse('logged out')
    #return redirect(request, 'accounts/login.html')



