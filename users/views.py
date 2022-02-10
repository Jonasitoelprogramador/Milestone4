from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Host, Worker
from hostofferings.models import Offering
from django.contrib.auth.models import User
from .forms import HostCreationForm, WorkerCreationForm
from hostofferings.forms import OfferingForm
from accounts.forms import UserEmailForm
from django.forms.models import model_to_dict
import random


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


@login_required()
def all_offerings(request):
    #get all the instances of the Host model
    hosts = Host.objects.all()
    result_list = []
    #loop through the instances
    for host in hosts:
        #get each offering associated with a given host
        offerings = Offering.objects.filter(host=host)
        offerings_list = list(offerings)
        #add offering and host together to results_list
        for o in offerings_list:
            host_and_offering = [host] + [o] + [o.pk]
            result_list += host_and_offering
    it = iter(result_list)
    zipped_tuples = zip(it, it, it)
    #create a list of tuples [host, offering]
    tuples = list(zipped_tuples)
    if str(request.user.type) == "host":
        return HttpResponse("You must be logged in as a worker to view this page")
    elif str(request.user.type) == "worker":
        context = {"inner_HTML": "Hosts",
            'offerings': tuples}
    return render(request, "hostofferings/all_offerings.html", context)


@login_required()
def all_workers(request):
    workers = Worker.objects.all()
    print(f"the workers list is {list(workers)}")
    lst_workers = list(workers)
    if str(request.user.type) == "worker":
        return HttpResponse("You must be logged in as a host to view this page")
    elif str(request.user.type) == "host":
        context = {"inner_HTML": "Workers",
            'workers': lst_workers}
    return render(request, "hostofferings/all_workers.html", context)


@login_required()
def offering_details(request, pk):
    #get all of the instances of the Offering model
    all_offerings = Offering.objects.all()
    #print out the primary key of all of the Offering model instances
    for o in all_offerings:
        print(o.pk)
    #get the offering instance with pk passed through the request
    offering_details = get_object_or_404(Offering, pk=pk)
    #get all of the Host model instances
    hosts = Host.objects.all()
    result_list = []
    #go through all of the Host model instances and get the offering instance
    #whose value for host matches the Host instance in that iteration.  Add
    #the matched offerings to the offerings_list.
    for host in hosts:
        offerings = Offering.objects.filter(host=host)
        offerings_list = list(offerings)
        #go thruogh the offerings_list and add each offering to a list with
        #its corresponding host.
        for o in offerings_list:
            host_and_offering = [host] + [o]
            result_list += host_and_offering
    #take the list and turn it into a list of tuples.
    it = iter(result_list)
    zipped_tuples = zip(it, it)
    tuples = list(zipped_tuples)
    #randomly select 3 elements from the tuples list
    lst = []
    i = 1
    while i < 4:
        ran_num = random.randint(0, len(tuples)-1)
        lst.append(tuples[ran_num])
        i += 1
    image = '/media/images/default.jpg'
    if str(request.user.type) == "host":
        return HttpResponse("You must be logged in as a worker to view this page")
    elif str(request.user.type) == "worker":
        context = {"inner_HTML": "Hosts",
            'offering_details': offering_details,
            'offerings': lst,
            'image': image}
    return render(request, "hostofferings/offering_details.html", context)


@login_required()
def worker_details(request, pk):
    all_workers = Worker.objects.all()
    all_workers_list = list(all_workers)
    print(all_workers_list)
    worker_details = get_object_or_404(Worker, pk=pk)
    #print out the primary key of all of the Offering model instances
    for w in all_workers:
        print(w.pk)
    #randomly select 3 elements from the tuples list
    lst = []
    i = 1
    while i < 4:
        ran_num = random.randint(0, len(all_workers_list)-1)
        lst.append(all_workers_list[ran_num])
        i += 1
    print(lst[0].first_language)
    image = '/media/images/default.jpg'
    if str(request.user.type) == "worker":
        return HttpResponse("You must be logged in as a host to view this page")
    elif str(request.user.type) == "host":
        context = {"inner_HTML": "Workers",
            'worker_details': worker_details,
            'workers': lst,
            'image': image}
    return render(request, "users/worker_details.html", context)
