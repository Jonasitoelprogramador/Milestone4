from .views import CreateCheckoutSessionView
from django.urls import re_path

urlpatterns = [ 
    re_path(r'^CreateCheckoutSessionView/$', CreateCheckoutSessionView, name='CreateCheckoutSessionView')
]