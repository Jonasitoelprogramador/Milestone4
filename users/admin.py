from django.contrib import admin
from .models import Host, Worker

# Register your models here.
admin.site.register(Host)
admin.site.register(Worker)