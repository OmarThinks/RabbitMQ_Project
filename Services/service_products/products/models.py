from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=3000)
    price = models.FloatField()


