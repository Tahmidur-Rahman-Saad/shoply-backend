from django.db import models
from users.models import Customer
from products.models import Product

# Create your models here.
class Cart(models.Model):
    cart_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE,null=None)

class CartItems(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE,null=None)
    amount = models.IntegerField(default=0)

class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True)
    confirmation = models.BooleanField(default = True)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE,null=None)

