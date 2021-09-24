from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import OfferingForm
from django.contrib.auth.decorators import login_required
from .models import offering
from django.apps import apps

# Create your views here.


@login_required()  
def add_offering(request):
    if request.method == "POST":
        print(request.user)
        form = OfferingForm(request.POST)
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
    offerings = offering.objects.all()
    hostModel = apps.get_model('users', 'Host')
    hosts = hostModel.objects.all()
    print(hosts)
    return render(request, "hostofferings/offering_marketplace.html", {'offerings': offerings, 'hosts': hosts})


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

