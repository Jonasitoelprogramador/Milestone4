from .views import profile
from django.urls import re_path

urlpatterns = [
    re_path('profile/', profile, name='Profile')
]