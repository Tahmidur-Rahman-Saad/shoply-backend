from rest_framework import serializers
from .models import Customer,AdminInfo


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
    
class AdminInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminInfo
        fields = '__all__'
        
    


