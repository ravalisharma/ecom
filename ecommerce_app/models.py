from django.db import models

# Create your models here.
class Product(models.Model):
    tittle=models.CharField(max_length=120)
    Description=models.TextField(max_length=50)
    Price=models.DecimalField(decimal_places=2,max_digits=20,default=39.99)
