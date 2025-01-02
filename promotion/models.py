from django.db import models

# Create your models here.

class Promotion(models.Model):
    start_date = models.DateTimeField( null = True,blank=True)
    end_date = models.DateTimeField( null = True,blank=True)
    image = models.ImageField(upload_to='discount_images/', null = True,blank=True)
    premium_profile_discount = models.IntegerField( null = True,blank=True)
    match_payment_discount = models.IntegerField( null = True,blank=True)
    title = models.CharField(max_length=255, null = True,blank=True)
    is_active = models.BooleanField( null = True,blank=True)
