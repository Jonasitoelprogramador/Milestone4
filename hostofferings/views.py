from django.shortcuts import render, HttpResponse
from .forms import offeringForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required()  
def add_offering(request):
    if request.method == "POST":
        form = offeringForm(request.POST)
        if form.is_valid():
            offering = form.save(commit=False)
            offering.host = request.user
            offering.save()
            return HttpResponse("added!")
        else:
            return HttpResponse("data not valid")
    else:
        form = offeringForm()
    return render(request, 'hostofferings/add_offering.html', {'form': form})
        