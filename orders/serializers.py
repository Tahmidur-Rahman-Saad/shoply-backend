from rest_framework import serializers
from .models import Cart, Order,CartItems

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'