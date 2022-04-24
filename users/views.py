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
from django.contrib.auth.decorators import user_passes_test
from products.models import Product

# The below functions are used in the docators that I have added in order to ensure good defensive design
# Checks if an instance of either a worker or host model exists
def host_worker_exist(user):
    try: 
        user.role
        host = ""
        worker = ""
        try: 
            user.worker
            worker = "yes"
        except:
            worker = "no"
        try: 
            user.host
            host = "yes"
        except:
            host = "no"
        if host == "yes" or worker == "yes":
            return True
        else:
            return False
    except:
        return True
        

# Checks if the user is associated with a host model instance
def host_check(user):
    try: 
        user.host
        return True
    except:
        return False


# Checks if the user is associated with a worker model instance
def worker_check(user):
    try: 
        user.worker
        return True
    except:
        return False


@login_required()
def profile(request):
    if str(request.user.role) == "host":
        current_user = request.user
        try:
            # get the host object associated with the logged in user
            host = Host.objects.get(user=current_user)
        except:
            host = None 
        try:
            offering = Offering.objects.filter(host=host).first()
        except:
            offering = None 
        
        # if the request is host, bind the inputted data to...
        if request.method == 'POST':
            #...HostCreationForm
            host_filled_form = HostCreationForm(request.POST, instance = host)
            if host_filled_form.is_valid():
                new_host = host_filled_form.save(commit=False)
                new_host.user = request.user
                new_host.save()
            #...OfferingForm
            offering_filled_form = OfferingForm(request.POST, request.FILES, instance = offering)
            if offering_filled_form.is_valid():
                offering = offering_filled_form.save(commit=False)
                offering.host = request.user.host
                offering.save()
            #...EmailForm
            user_email_filled_form = UserEmailForm(request.POST, instance = request.user)
            if user_email_filled_form.is_valid():
                user_email_filled_form.save()

        else:
            host_filled_form = HostCreationForm(instance=host)
            offering_filled_form = OfferingForm(instance=offering)
            user_email_filled_form = UserEmailForm(instance=request.user)
        # define values for context in order to hide unwanted navbar links
        try: 
            str(request.user.host)
            headerhidden = ""
            if str(request.user.host.payment_status) == "paid":
                upgrade_hidden = "hidden"
            else:
                upgrade_hidden = ""
        except:
            upgrade_hidden = ""
            headerhidden = "hidden"

        context = {
            "filled_form": host_filled_form, 
            'offering_filled_form': offering_filled_form, 
            'user_email_filled_form': user_email_filled_form, 
            'user_obj': request.user,
            'off_obj': offering,
            "inner_HTML": "Workers",
            "upgradeHidden": upgrade_hidden,
            "profile": "Profile",
            "login_logout": "Logout",
            "headerhidden": headerhidden,
            "products": Product.objects.all()
        }
        if request.user.is_superuser:
            context['admin'] = "Admin Access"

        return render(request, 'users/host_profile.html', context)
    
    elif str(request.user.role) == "worker":
        current_user = request.user
        #get the worker instance associated with the logged in user
        try:
            worker = Worker.objects.get(user=current_user)
        except:
            worker = None 
        
        # if the request is host, bind the inputted data to...
        if request.method == 'POST':
            #...WorkerCreationForm
            worker_filled_form = WorkerCreationForm(request.POST, request.FILES, instance = worker)
            if worker_filled_form.is_valid():
                new_worker = worker_filled_form.save(commit=False)
                new_worker.user = request.user
                new_worker.save()
            #...UserEmailForm
            user_email_filled_form = UserEmailForm(request.POST, instance = request.user)
            if user_email_filled_form.is_valid():
                user_email_filled_form.save()

        else:
            worker_filled_form = WorkerCreationForm(instance=worker)
            user_email_filled_form = UserEmailForm(instance=request.user)
        # define values for context in order to hide unwanted navbar links
        try:
            str(request.user.worker)
            headerhidden = ""
            if str(request.user.worker.payment_status) == "paid":
                upgrade_hidden = "hidden"
            else:
                upgrade_hidden = ""
        except:
            upgrade_hidden = ""
            headerhidden = "hidden"

        context = {
            "filled_form": worker_filled_form, 
            'user_email_filled_form': user_email_filled_form, 
            'user_obj': request.user,
            'worker': worker,
            "inner_HTML": "Hosts",
            "upgradeHidden": upgrade_hidden,
            "profile": "Profile",
            "login_logout": "Logout",
            "headerhidden": headerhidden,
            "products": Product.objects.all()
        }
        if request.user.is_superuser:
            context['admin'] = "Admin Access"

        return render(request, 'users/worker_profile.html', context)


@user_passes_test(worker_check, login_url="/")
@user_passes_test(host_worker_exist, login_url="/users/profile")
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
            host_and_offering = [host] + [o]
            result_list += host_and_offering
    it = iter(result_list)
    zipped_tuples = zip(it, it)
    #create a list of tuples [host, offering]
    tuples = list(zipped_tuples)
    if str(request.user.role) == "host":
        return HttpResponse("You must be logged in as a worker to view this page")
    elif str(request.user.role) == "worker":
        if str(request.user.worker.payment_status) == "paid":
            upgrade_hidden = "hidden"
        else:
            upgrade_hidden = ""
        context = {
            "inner_HTML": "Hosts",
            'offerings': tuples,
            "upgradeHidden": upgrade_hidden,
            "profile": "Profile",
            "login_logout": "Logout",
            "products": Product.objects.all()
        }
        if request.user.is_superuser:
            context['admin'] = "Admin Access"
    return render(request, "hostofferings/all_offerings.html", context)


@user_passes_test(host_check, login_url="/")
@user_passes_test(host_worker_exist, login_url="/users/profile")
@login_required()
def all_workers(request):
    #get all the instances of the Worker model
    workers = Worker.objects.all()
    lst_workers = list(workers)
    if str(request.user.role) == "worker":
        return HttpResponse("You must be logged in as a host to view this page")
    # check that user is a host and has paid
    elif str(request.user.role) == "host":
        if str(request.user.host.payment_status) == "paid":
            upgrade_hidden = "hidden"
        else:
            upgrade_hidden = ""
        # set context to pass navbar values to frontend
        context = {
            "inner_HTML": "Workers",
            'workers': lst_workers,
            "upgradeHidden": upgrade_hidden,
            "profile": "Profile",
            "login_logout": "Logout",
            "products": Product.objects.all()
            }
        if request.user.is_superuser:
            context['admin'] = "Admin Access"
    return render(request, "hostofferings/all_workers.html", context)


@user_passes_test(worker_check, login_url="/")
@user_passes_test(host_worker_exist, login_url="/users/profile")
@login_required()
def offering_details(request, pk):
    #get all of the instances of the Offering model
    all_offerings = Offering.objects.all()
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
        if tuples[ran_num] not in lst and tuples[ran_num][1] != offering_details:
            lst.append(tuples[ran_num])
            i += 1
    image = '/media/images/default.jpg'
    if str(request.user.role) == "host":
        return HttpResponse("You must be logged in as a worker to view this page")
    elif str(request.user.role) == "worker":
        if request.user.worker.payment_status == "paid":
            #this needs to be the email of the host instance
            email_parameter = offering_details.host.user.email
            upgrade_hidden = "hidden"
        elif request.user.worker.payment_status == "nonpaid":
            email_parameter = "Upgrade your account to access host's email!"
            upgrade_hidden = ""
        context = {
            "inner_HTML": "Hosts",
            'offering_details': offering_details,
            'offerings': lst,
            'image': image,
            'email': email_parameter,
            "upgradeHidden": upgrade_hidden,
            "profile": "Profile",
            "login_logout": "Logout",
            "products": Product.objects.all()
        }
        if request.user.is_superuser:
            context['admin'] = "Admin Access"
    return render(request, "hostofferings/offering_details.html", context)


@user_passes_test(host_check, login_url="/")
@user_passes_test(host_worker_exist, login_url="/users/profile")
@login_required()
def worker_details(request, pk):
    all_workers = Worker.objects.all()
    all_workers_list = list(all_workers)
    worker_details = get_object_or_404(Worker, pk=pk)
    #randomly select 3 elements from the tuples list
    lst = []
    i = 1
    while i < 4:
        ran_num = random.randint(0, len(all_workers_list)-1)
        if all_workers_list[ran_num] not in lst and all_workers_list[ran_num] != worker_details:
            lst.append(all_workers_list[ran_num])
            i += 1
    image = '/media/images/default.jpg'
    if str(request.user.role) == "worker":
        return HttpResponse("You must be logged in as a host to view this page")
    elif str(request.user.role) == "host":
        if request.user.host.payment_status == "paid":
            #this needs to be the email of the worker instance
            email_parameter = worker_details.user.email
            upgrade_hidden = "hidden"
        elif request.user.host.payment_status == "nonpaid":
            email_parameter = "Upgrade your account to access worker's email!"
            upgrade_hidden = ""
        context = {
            "inner_HTML": "Workers",
            'worker_details': worker_details,
            'workers': lst,
            'image': image,
            'email': email_parameter,
            "upgradeHidden": upgrade_hidden,
            "profile": "Profile",
            "login_logout": "Logout",
            "products": Product.objects.all()
            }
        if request.user.is_superuser:
            context['admin'] = "Admin Access"
    return render(request, "users/worker_details.html", context)


