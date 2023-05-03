from django.db import models
class ProductDetails(models.Model):
    product_name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    quantity=models.IntegerField()
    price=models.FloatField()
# Create your models here.
