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


#custom serializer for retrieving customer or admin data
class UserReadSerializer(serializers.ModelSerializer):
    additional_info = serializers.SerializerMethodField('get_additional_info')

    def get_additional_info(self, instance ):

        if not instance.is_staff:
            info = Customer.objects.get(user = instance.id)
            return CustomerSerializer(info).data
        else:
            info = AdminInfo.objects.get(user = instance.id)
            return AdminInfoSerializer(info).data
        


    class Meta:
        model = User
        fields = '__all__'
    

