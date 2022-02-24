from users.views import profile, all_offerings, offering_details, all_workers, worker_details, hello_time
from django.urls import re_path


urlpatterns = [
    re_path('profile/', profile, name='profile'), 
    re_path(r'^all_offerings/$', all_offerings, name='all_offerings'),
    re_path(r'^offering_details/(?P<pk>\d+)/$', offering_details, name="offering_details"),
    re_path(r'^all_workers/$', all_workers, name='all_workers'),
    re_path(r'^worker_details/(?P<pk>\d+)/$', worker_details, name='worker_details'),
    re_path(r'^hello_time/$', hello_time, name='hello_time')
    ]