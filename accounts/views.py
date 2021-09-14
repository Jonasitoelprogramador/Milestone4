from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
        else:
            print(user_form.errors)
    
    
    #else:
        #messages.error(request, "unable to log you in at this time!")
    form = UserCreationForm()
    return render(request, 'accounts/index.html', {'form': form})