from .views import hostProfile, workerProfile
from django.urls import re_path

urlpatterns = [
    re_path('hostprofile/', hostProfile, name='hostprofile'),
    re_path('workerprofile/', workerProfile, name='workerprofile'),
]