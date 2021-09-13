from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
    
    user = authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))
    
    if user:
                login(request, user)
                messages.success(request, "You have successfully registered")
                return HttpResponse("butt bois beer")
                

    else:
        messages.error(request, "unable to log you in at this time!")
    return HttpResponse("va fan culo")