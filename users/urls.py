from .views import hostProfile
from django.urls import path

urlpatterns = [
    path('hostprofile/', hostProfile, name='hostprofile'),
]