from django.db import models
from users.models import Host
import os
import time 
import random
import string
import os.path


def path_time(instance, filename):
    print("hello I need to make a path time as quickly as possible becos running late")
    #takes the instance and the filename of the uploaded image
    #splits the filename from the extension
    extension = os.path.splitext(filename)[1]
    #assigns a random value to the random_identifier field of the model instance
    instance.random_identifier = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    #adds the correct file extension to this field
    instance.random_identifier = instance.random_identifier + extension
    print(f'this is the identofier {instance.random_identifier}')
    upload = 'media/images/'
    #uploads the newly-renamed image to the images folder on the server
    print(f'this is the path I am using {os.path.join(upload, instance.random_identifier)}')
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

