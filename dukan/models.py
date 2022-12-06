from django.db import models

# Create your models here.

class Seller(models.Model):

    brand_name = models.CharField(max_length=100)
    seller_name = models.CharField(max_length=100)

    brand_id = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):  
        return self.brand_name