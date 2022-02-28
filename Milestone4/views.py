from django.shortcuts import render
import os


def homepage(request):
    worker = "worker"
    host = "host"
    # if user is logged in
    if str(request.user) != 'AnonymousUser':
        profile = "Profile"
        logout = "Logout"
        # check the user is a host
        if str(request.user.role) == "host":
            # depending on the user role and payment status, different values
            # are assigned to the variables in the context section
            inner_HTML = 'Workers'
            try: 
                str(request.user.host)
                if str(request.user.host.payment_status) == "paid":
                    upgrade_hidden = "hidden"
                else:
                    upgrade_hidden = ""
            except:
                upgrade_hidden = ""
        # check the user is a worker
        elif str(request.user.role) == "worker":
            # depending on the user role and payment status, different values
            # are assigned to the variables in the context section
            inner_HTML = 'Hosts'
            try: 
                str(request.user.worker)
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
        # if user is not logged in
        return render(request, 'accounts/homepage.html', {"login_logout": "Login", "hidden": "hidden", "upgradeHidden": "hidden"})    

