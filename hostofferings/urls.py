from hostofferings.views import add_offering, all_offerings, offering_details, delete_offering, edit_offering
from django.conf.urls import url

urlpatterns = [ 
    url(r'^add_offering/$', add_offering, name='add_offering'),
    url(r'^all_offerings/$', all_offerings, name='all_offerings'),
    url(r'^offering_details/(?P<pk>\d+)/$', offering_details, name="offering_details"),
    url(r'^delete/(?P<pk>\d+)/$', delete_offering, name='delete_offering'),
    url(r'^edit_offering/(?P<pk>\d+)/$', edit_offering, name='edit_offering')]