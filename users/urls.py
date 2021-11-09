from .views import hostProfile, hostProfileEdit
from django.urls import path

urlpatterns = [
    path('hostprofile/', hostProfile, name='hostprofile'),
    path('hostprofileedit/', hostProfileEdit, name='hostprofileedit'),
]