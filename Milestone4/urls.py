"""Milestone4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from accounts.views import register, login, profile, logout
from hostofferings.views import add_offering, all_offerings, offering_details


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register/$', register, name="register"),
    url(r'^login/$', login, name='login'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^add_offering/$', add_offering, name='add_offering'),
    url(r'^all_offerings/$', all_offerings, name='all_offerings'),
    url(r'^offering_details/(?P<pk>\d+)/$', offering_details, name="offering_details")
]