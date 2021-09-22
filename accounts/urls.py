from .views import register, login, profile, logout  #addHost
from django.conf.urls import url
from django.urls import path

urlpatterns = [     
    path('register/<user_type>/', register, name="register"),
    url('login/', login, name='login'),
    url('profile/', profile, name='profile'),
    url('logout/', logout, name='logout')]
  #  url(r'^add_host/$', addHost, name='add_host')