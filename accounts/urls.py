from .views import login, logout 
from django.urls import path

urlpatterns = [     
    #path('register/<user_type>/', register, name="register"),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')]