from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Host
from hostofferings.models import offering
from django.contrib.auth.models import User
from hostofferings.forms import OfferingForm
from .forms import HostForm
from accounts.forms import ExtendedUserCreationForm


@login_required()
def hostProfile(request):  
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
    return render(request, 'users/host_profile.html', {'host': hoster, 'offer': offer})


@login_required()
def hostProfileEdit(request):
    offeringz = offering.objects.all()
    userz = User.objects.all()
    result_list = []
    hosts = Host.objects.all()
    if request.method == 'POST':
        for h in hosts:
                if request.user == h.user:
                    print(h)
               #     return h
        hostyForm = HostForm(request.POST, instance = h)
        if hostyForm.is_valid():
            hostyForm.save()
         #   render(request, 'users/host_profile.html')
    #else:
    for h in hosts:
        if request.user == h.user:
            hostDict = {'nationality': h.nationality, 'first_language': h.first_language, 'location': h.location}
    host_filled_form = HostForm(initial=hostDict)
    for o in offeringz:
        if request.user == o.host.user:
            offDict = {'work_category': o.work_category, 'work_details': o.work_details}
    offering_filled_form = OfferingForm(initial=offDict)
    for u in userz:
        if request.user == u:
            userDict = {'email': u.email}
    user_filled_form = ExtendedUserCreationForm(initial=userDict)
    return render(request, 'users/host_profile_edit.html', {"host_filled_form": host_filled_form,
    'offering_filled_form': offering_filled_form, 'user_filled_form': user_filled_form})