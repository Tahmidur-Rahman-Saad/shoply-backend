from django.db import models
from users.models import User
from products.models import Product

# Create your models here.
class Cart(models.Model):
    cart_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

class CartItems(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE,default=None)
    amount = models.IntegerField()

class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True)
    confirmation = models.BooleanField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE,default=None)

