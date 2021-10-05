from django.db import models
from users.models import Host


def path_and_rename(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        pass
    # return the whole path to the file
    return os.path.join(upload_to, filename)


# Create your models here.
class offering(models.Model):
    work_category = models.CharField(max_length=100)
    work_details = models.TextField()
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    offering_image = models.ImageField(upload_to=path_and_rename, default='default.jpg')

    def __str__(self):
        return self.work_category

