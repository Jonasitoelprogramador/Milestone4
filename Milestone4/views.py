from django.shortcuts import render


def homepage(request):
    worker = "worker"
    host = "host"
    if str(request.user) != 'AnonymousUser':
        if str(request.user.type) == "host":
            return render(request, 'accounts/homepage.html', {"inner_HTML": "Hosts"})
        elif str(request.user.type) == "worker":
            return render(request, 'accounts/homepage.html', {"inner_HTML": 'Workers'})
    else:
        return render(request, 'accounts/homepage.html')    

