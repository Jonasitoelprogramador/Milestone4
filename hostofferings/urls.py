from .views import add_offering, all_offerings, offering_details, delete_offering, edit_offering, all_workers
from django.urls import re_path

urlpatterns = [ 
    re_path(r'^add_offering/$', add_offering, name='add_offering'),
    re_path(r'^all_offerings/$', all_offerings, name='all_offerings'),
    re_path(r'^offering_details/(?P<pk>\d+)/$', offering_details, name="offering_details"),
    re_path(r'^delete/(?P<pk>\d+)/$', delete_offering, name='delete_offering'),
    re_path(r'^edit_offering/(?P<pk>\d+)/$', edit_offering, name='edit_offering'),
    re_path(r'^all_workers/$', all_workers, name='all_workers')]