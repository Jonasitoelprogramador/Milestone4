from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def hostProfile(request):
    return render(request, 'users/host_profile.html')


