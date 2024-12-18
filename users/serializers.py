from rest_framework import serializers
from .models import Customer,AdminInfo
from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
    
class AdminInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminInfo
        fields = '__all__'
        
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username','first_name','last_name','email','password']
        fields = '__all__'
