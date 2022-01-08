from django.db import models
from users.models import Host
import os
import time 
import random
import string
import os.path


def path_time(instance, filename):
    extension = os.path.splitext(filename)[1]
    instance.random_identifier = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    instance.random_identifier = instance.random_identifier + extension
    print(instance.random_identifier)
    upload = 'images/'
    return os.path.join(upload, instance.random_identifier)


# Create your models here.
class Offering(models.Model):
    work_category = models.CharField(max_length=100)
    work_details = models.TextField()
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    offering_image = models.ImageField(upload_to=path_time, default='default.jpg')
    random_identifier = models.CharField(max_length=100)

    def __str__(self):
        return self.work_category

