from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=50,unique=True)

    def __str__(self):
        return self.name

