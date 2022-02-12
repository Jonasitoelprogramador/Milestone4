from django.shortcuts import render


def homepage(request):
    worker = "worker"
    host = "host"
    if str(request.user.type) == "host":
       return render(request, 'accounts/homepage.html', {"host_or_worker": host})
    elif str(request.user.type) == "worker":
        return render(request, 'accounts/homepage.html', {"host_or_worker": worker})
