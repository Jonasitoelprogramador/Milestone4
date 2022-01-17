from .views import hostProfile, workerProfile, hostOrWorker
from django.urls import re_path

urlpatterns = [
    re_path('hostprofile/', hostProfile, name='hostprofile'),
    re_path('workerprofile/', workerProfile, name='workerprofile'),
    re_path('hostorworker/', hostOrWorker, name='hostorworker'),
]