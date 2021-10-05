from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import OfferingForm
from django.contrib.auth.decorators import login_required
from .models import offering
from django.apps import apps
from .models import Host




# Create your views here.


@login_required()  
def add_offering(request):
    if request.method == "POST":
        print(request.user)
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
    hosts = Host.objects.all()
    result_list = []
    for host in hosts:
        offerings = offering.objects.filter(host=host)
        offerings_list = list(offerings)
        for o in offerings_list:
            host_and_offering = [host] + [o]
            result_list += host_and_offering
    it = iter(result_list)
    zipped_tuples = zip(it, it)
    tuples = list(zipped_tuples)
    image = '/media/images/default.jpg'
    print(tuples)
    return render(request, "hostofferings/all_offerings.html", {'offerings': tuples, 'image': image})


@login_required()
def offering_details(request, pk):
    offering_details = get_object_or_404(offering, pk=pk)
    print(offering_details)
    return render(request, 'hostofferings/offering_details.html', {'offering_details': offering_details})


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
        offer = offering.objects.get(pk=pk)
        form = OfferingForm(instance=offer)
    return render(request, 'hostofferings/add_offering.html', {'form': form})


@login_required()
def marketplace(request):
    return render(request, 'hostofferings/home.html')