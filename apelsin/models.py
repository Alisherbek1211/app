from email.policy import default
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.CharField(max_length=255)
