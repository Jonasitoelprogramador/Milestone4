from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Host
from hostofferings.models import offering
from hostofferings.forms import OfferingForm
from .forms import HostForm


@login_required()
def hostProfile(request):
    offeringform =  OfferingForm()
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
    for x in tuples:
        if x[0] == request.user: 
            return x
    hoster = x[0]
    offer = x[1]
    for h in hosts:
        if request.user == h.user:
            d = {'nationality': h.nationality, 'first_language': h.first_language, 'location': h.location}
    filled_form = HostForm(initial=d)
    return render(request, 'users/host_profile.html', {'host': hoster, 'offer': offer, "filled_form": filled_form})


