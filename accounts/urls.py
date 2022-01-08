from .views import login, logout 
from django.urls import re_path

urlpatterns = [     
    re_path('login/', login, name='login'),
    re_path('logout/', logout, name='logout')]