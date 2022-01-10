from .views import hostProfile #hostProfileEdit
from django.urls import re_path

urlpatterns = [
    re_path('hostprofile/', hostProfile, name='hostprofile'),
    #re_path('hostprofileedit/', hostProfileEdit, name='hostprofileedit'),
]