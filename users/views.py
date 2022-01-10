from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Host
from hostofferings.models import Offering
from django.contrib.auth.models import User
from .forms import HostCreationForm
from hostofferings.forms import OfferingForm
from accounts.forms import UserEmailForm
from django.forms.models import model_to_dict

 

'''@login_required()
def hostProfile(request):  
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
    hosts = Host.objects.all() 
    result_list = []
    for host in hosts:
        offerings = Offering.objects.filter(host=host)
        offerings_list = list(offerings)
        for o in offerings_list:
            host_and_offering = [host] + [o]
            result_list += host_and_offering
    it = iter(result_list)
    zipped_tuples = zip(it, it)
    tuples = list(zipped_tuples)
    for x in tuples:
        if x[0] == request.user: 
            context = {
                'host': x[0],
                'offer': x[1]}
        else:
            context = {}
    return render(request, 'users/host_profile.html', context)'''


@login_required()
def hostProfile(request):
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
        print(f"The host filled form:{host_filled_form}")
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
        "host_filled_form": host_filled_form, 
        'offering_filled_form': offering_filled_form, 
        'user_email_filled_form': user_email_filled_form, 
        'user_obj': request.user,
        'off_obj': offering
    }
    
    return render(request, 'users/host_profile_edit.html', context)


        # this_is_snake_case
    


    # try:
    #     host = Host.objects.get(user=current_user)
    # except ObjectDoesNotExist as e:
    #     print(e)
    #     # think about what you'd want to happen if there wasn't a host


    # offeringz = offering.objects.all()
    # userz = User.objects.all()
    # result_list = []
    # hosts = Host.objects.all()
    # for h in hosts:
    #     if (request.user == h.user):
    #         if (request.method == 'POST'):
    #             hostyForm = HostCreationForm(request.POST, instance = h)
    #             saveForm(hostyForm)
    #         else:    
    #             hostDict = {'nationality': h.nationality, 'first_language': h.first_language, 'location': h.location}
    #             host_filled_form = HostCreationForm(initial=hostDict)
    # for o in offeringz:
    #     if (request.user == o.host.user):
    #         if (request.method == 'POST'):
    #             off_obj = o
    #             #associate the post request with the correct instance of the model
    #             offeryForm = OfferingForm(request.POST, request.FILES, instance = o)
    #             print(f"offeryForm.data: {offeryForm.data}")
    #             saveForm(offeryForm)
    #         else:
    #             off_obj = o
    #             offDict = {'work_category': o.work_category, 'work_details': o.work_details, 'offering_image': o.offering_image}
    #             offering_filled_form = OfferingForm(initial=offDict)
    # for u in userz:
    #     if request.user == u:
    #         user_obj = u 
    #         if request.method == 'POST':
    #             print(request.POST)
    #             useryForm = UserEmailForm(request.POST, instance = u)
    #             saveForm(useryForm)
    #             return render(request, 'users/host_profile_edit.html')
    #         else:
    #             userDict = {'email': u.email}
    #             user_email_filled_form = UserEmailForm(initial=userDict) 
    # return render(request, 'users/host_profile_edit.html', {"host_filled_form": host_filled_form, 
    #         'offering_filled_form': offering_filled_form, 'user_email_filled_form': user_email_filled_form, 'user_obj': user_obj,
    #         'off_obj': off_obj})


def saveForm(formToSave):
    counter = 0
    if formToSave.is_valid():
        formToSave.save()
        counter += 1
    else:
        print("not valid")


