from django.shortcuts import render


def homepage(request):
    worker = "worker"
    host = "host"
    print(f"playing the game of one two three {request.user.type}")
    if str(request.user) != 'AnonymousUser':
        if str(request.user.type) == "host":
            return render(request, 'accounts/homepage.html', {"inner_HTML": "Workers"})
        elif str(request.user.type) == "worker":
            return render(request, 'accounts/homepage.html', {"inner_HTML": 'Hosts'})
    else:
        return render(request, 'accounts/homepage.html')    

