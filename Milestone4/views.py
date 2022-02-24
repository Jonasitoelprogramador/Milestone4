from django.shortcuts import render
import os

print(os.environ)


def homepage(request):
    worker = "worker"
    host = "host"
    if str(request.user) != 'AnonymousUser':
        profile = "Profile"
        logout = "Logout"
        if str(request.user.role) == "host":
            inner_HTML = 'Workers'
            try: 
                str(request.user.host)
                if str(request.user.host.payment_status) == "paid":
                    upgrade_hidden = "hidden"
                else:
                    upgrade_hidden = ""
            except:
                upgrade_hidden = ""
        elif str(request.user.role) == "worker":
            inner_HTML = 'Hosts'
            try: 
                str(request.user.host)
                if str(request.user.worker.payment_status) == "paid":
                    upgrade_hidden = "hidden"
                else:
                    upgrade_hidden = ""
            except:
                upgrade_hidden = ""
        context = {
            "inner_HTML": inner_HTML,
            "upgradeHidden": upgrade_hidden,
            "profile": profile,
            "login_logout": logout
        }
        return render(request, 'accounts/homepage.html', context)
    else:
        return render(request, 'accounts/homepage.html', {"login_logout": "Login", "hidden":"hidden"})    

