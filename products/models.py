from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    weight = models.CharField(max_length=120)
    price = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()