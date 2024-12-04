from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    details = models.TextField(max_length=100)
    image = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,default=None)


