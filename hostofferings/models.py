from django.db import models
from users.models import Host

# Create your models here.
class offering(models.Model):
    work_category = models.CharField(max_length=100)
    work_details = models.TextField()
    host = models.ForeignKey(Host, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

