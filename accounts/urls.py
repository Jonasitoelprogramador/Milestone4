from .views import login, logout, signup 
from django.urls import re_path

urlpatterns = [     
    re_path('login/', login, name='login'),
    re_path('logout/', logout, name='logout'),
    re_path('signup/', signup, name='signup')]
