from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customers', null = True)
    phone = models.CharField(max_length=15,null=True,blank=True,)
    

    


class AdminInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admininfo')
    phone = models.CharField(max_length=15,null=True,blank=True,)
    nid = models.CharField(max_length=11,null = True,blank=True,)
    image = models.ImageField( upload_to='uploads/', height_field=None, width_field=None, max_length=None)
    


