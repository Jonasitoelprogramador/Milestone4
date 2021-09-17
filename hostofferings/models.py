from django.db import models
from django.contrib.auth.models import hosts

# Create your models here.
class offering(models.Model):
    work_category = models.CharField(max_length=100)
    work_details = models.TextField()
    host = models.ForeignKey(hosts, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name