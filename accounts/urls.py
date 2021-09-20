from .views import register, login, profile, logout, addHost
from django.conf.urls import url

urlpatterns = [     
    url(r'^register/$', register, name="register"),
    url(r'^login/$', login, name='login'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^add_host/$', addHost, name='add_host')]