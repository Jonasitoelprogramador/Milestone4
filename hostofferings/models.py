from django.db import models
from users.models import Host


# Create your models here.
class offering(models.Model):
    work_category = models.CharField(max_length=100)
    work_details = models.TextField()
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    offering_image = models.ImageField(upload_to='images/', default='default.jpg')

    def __str__(self):
        return self.work_category

