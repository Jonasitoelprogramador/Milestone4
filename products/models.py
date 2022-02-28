from django.db import models

# Create your models here.
# simple model with 3 attributes
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=2000)
    price_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    # used to change the price from cents (as in Stripe) to dollars
    def get_display_price(self):
        return "{0:.02f}".format(self.price / 100)
