from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Host
from hostofferings.models import offering
from hostofferings.forms import OfferingForm
from .forms import HostForm
import pathlib
from PIL import Image
import os
# from constants import MEDIA_FILEPATH

MEDIA_FILEPATH = pathlib.Path(__file__).parents[1].resolve() / "media"



@login_required()
def hostProfile(request):
    hosts = Host.objects.all()
    offeringz = offering.objects.all()
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
            hostDict = {'nationality': h.nationality, 'first_language': h.first_language, 'location': h.location}
    host_filled_form = HostForm(initial=hostDict)
    for o in offeringz:
        if request.user == o.host.user:
            offDict = {'work_category': o.work_category, 'work_details': o.work_details}
    offering_filled_form = OfferingForm(initial=offDict)
    return render(request, 'users/host_profile.html', {'host': hoster, 'offer': offer, "host_filled_form": host_filled_form, 'offering_filled_form': offering_filled_form})


