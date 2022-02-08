from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import OfferingForm
from django.contrib.auth.decorators import login_required
from .models import Offering
from django.apps import apps
import random
from users.models import Host, Worker


# Create your views here.
@login_required()  
def add_offering(request):
    if request.method == "POST":
        print(request.user)
        print(f"request.POST: {request.POST} - request.FILES: {request.FILES}")
        form = OfferingForm(request.POST, request.FILES)
        if form.is_valid():
            offering = form.save(commit=False)
            try:
                offering.host = request.user.host
                offering.save()
                return HttpResponse("added!")
            except:
                return HttpResponse("Cannot add an offering as a worker")
        else:
            return HttpResponse("data not valid")
    else:
        form = OfferingForm()
    return render(request, 'hostofferings/add_offering.html', {'form': form})


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
    all_workers = Offering.objects.all()
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
def delete_offering(request, pk):
    current_offering = get_object_or_404(offering, pk=pk) 
    current_offering.delete()
    return redirect('profile')
    

@login_required()  
def edit_offering(request, pk):
    if request.method == "POST":
        form = OfferingForm(request.POST)
        if form.is_valid():
            current_offering = form.save(commit=False)
            current_offering.host = request.user
            current_offering.save()
            return HttpResponse("edited!")
        else:
            return HttpResponse("data not valid")
    else:
        offer = Offering.objects.get(pk=pk)
        form = OfferingForm(instance=offer)
    return render(request, 'hostofferings/add_offering.html', {'form': form})


@login_required()
def marketplace(request):
    return render(request, 'hostofferings/home.html')