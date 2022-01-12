from django.db import models

class Type(models.Model):
    work_category = models.CharField(max_length=100)
    account_choices = [
        ('host', 'host'),
        ('worker', 'worker')]
    account_type = models.CharField(
        max_length=6,
        choices=account_choices)

    def __str__(self):
        return self.account_type

        
        




