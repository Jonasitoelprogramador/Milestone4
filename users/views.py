from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Host
from hostofferings.models import offering
from django.contrib.auth.models import User
from hostofferings.forms import OfferingForm
from .forms import HostForm
from accounts.forms import UserEmailForm
from django.forms.models import model_to_dict
from copy import copy
from django.contrib.auth import authenticate, login


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
    for h in hosts:
        if request.user == h.user:
            if request.method == 'POST':
                hostyForm = HostForm(request.POST, instance = h)
                saveForm(hostyForm)
            else:    
                hostDict = {'nationality': h.nationality, 'first_language': h.first_language, 'location': h.location}
                host_filled_form = HostForm(initial=hostDict)
    for o in offeringz:
        if request.user == o.host.user:
            if request.method == 'POST':
                offeryForm = OfferingForm(request.POST, instance = o)
                saveForm(offeryForm)
            else:
                offDict = {'work_category': o.work_category, 'work_details': o.work_details}
                offering_filled_form = OfferingForm(initial=offDict)
    for u in userz:
        if request.user == u:
            if request.method == 'POST':
                print(request.POST)
                useryForm = UserEmailForm(request.POST, instance = u)
                saveForm(useryForm)
                return render(request, 'users/host_profile_edit.html')
            else:
                userDict = {'email': u.email}
                user_filled_form = UserEmailForm(initial=userDict)
    return render(request, 'users/host_profile_edit.html', {"host_filled_form": host_filled_form, 
            'offering_filled_form': offering_filled_form, 'user_filled_form': user_filled_form})


def saveForm(formToSave):
    counter = 0
    if formToSave.is_valid():
        formToSave.save()
        counter += 1
    else:
        print("not valid")


#This is based on stack overflow: https://stackoverflow.com/questions/8216353/django-update-one-field-using-modelform
def UPOST(post, obj):
    '''Updates request's POST dictionary with values from object, for update purposes'''
    post = copy(post)
    for k,v in model_to_dict(obj).items():
        if k == "username": post[k] = v
        if k == "first_name": post[k] = v
        if k == "last_name": post[k] = v
    if authenticate(username=post["username"], password=post["password1"]):
        login(post, post["username"])
        post["password2"] = post["password1"]
    print(post)
    return post

