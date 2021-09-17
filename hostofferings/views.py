from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import OfferingForm
from django.contrib.auth.decorators import login_required
from .models import offering

# Create your views here.

@login_required()  
def add_offering(request):
    if request.method == "POST":
        form = offeringForm(request.POST)
        if form.is_valid():
            offering = form.save(commit=False)
            offering.host = request.user
            offering.save()
            return HttpResponse("added!")
        else:
            return HttpResponse("data not valid")
    else:
        form = offeringForm()
    return render(request, 'hostofferings/add_offering.html', {'form': form})


@login_required()
def all_offerings(request):
    offerings = offering.objects.all()
    return render(request, "hostofferings/offering_marketplace.html", {'offerings': offerings})


@login_required()
def offering_details(request, pk):
    offering_details = get_object_or_404(offering, pk=pk)
    print(offering_details)
    return render(request, 'hostofferings/offering_details.html', {'offering_details': offering_details})
    
    