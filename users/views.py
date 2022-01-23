from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Host, Worker
from hostofferings.models import Offering
from django.contrib.auth.models import User
from .forms import HostCreationForm, WorkerCreationForm
from hostofferings.forms import OfferingForm
from accounts.forms import UserEmailForm
from django.forms.models import model_to_dict
from accounts.urls import urlpatterns


@login_required()
def profile(request):
    if str(request.user.type) == "host":
        current_user = request.user
        try:
            host = Host.objects.get(user=current_user)
        except:
            host = None 
        # you want to force a 1:1 between offering and host
        try:
            offering = Offering.objects.filter(host=host).first()
        except:
            offering = None 
        
        if request.method == 'POST':
            host_filled_form = HostCreationForm(request.POST, instance = host)
            if host_filled_form.is_valid():
                new_host = host_filled_form.save(commit=False)
                new_host.user = request.user
                new_host.save()
            offering_filled_form = OfferingForm(request.POST, request.FILES, instance = offering)
            if offering_filled_form.is_valid():
                offering = offering_filled_form.save(commit=False)
                offering.host = request.user.host
                offering.save()
            user_email_filled_form = UserEmailForm(request.POST, instance = request.user)
            if user_email_filled_form.is_valid():
                user_email_filled_form.save()

        else:
            host_filled_form = HostCreationForm(instance=host)
            offering_filled_form = OfferingForm(instance=offering)
            user_email_filled_form = UserEmailForm(instance=request.user)

        context = {
            "filled_form": host_filled_form, 
            'offering_filled_form': offering_filled_form, 
            'user_email_filled_form': user_email_filled_form, 
            'user_obj': request.user,
            'off_obj': offering
        }
        
        return render(request, 'users/host_profile.html', context)
    
    elif str(request.user.type) == "worker":
        current_user = request.user
        #get the worker instance associated with the logged in user
        try:
            worker = Worker.objects.get(user=current_user)
        except:
            worker = None 
        # you want to force a 1:1 between offering and host 
        
        if request.method == 'POST':
            worker_filled_form = WorkerCreationForm(request.POST, request.FILES, instance = worker)
            if worker_filled_form.is_valid():
                new_worker = worker_filled_form.save(commit=False)
                new_worker.user = request.user
                new_worker.save()
            user_email_filled_form = UserEmailForm(request.POST, instance = request.user)
            if user_email_filled_form.is_valid():
                user_email_filled_form.save()

        else:
            worker_filled_form = WorkerCreationForm(instance=worker)
            user_email_filled_form = UserEmailForm(instance=request.user)

        context = {
            "filled_form": worker_filled_form, 
            'user_email_filled_form': user_email_filled_form, 
            'user_obj': request.user,
            'worker': worker
        }
        
        return render(request, 'users/worker_profile.html', context)



def saveForm(formToSave):
    counter = 0
    if formToSave.is_valid():
        formToSave.save()
        counter += 1
    else:
        print("not valid")


