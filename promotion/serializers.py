from rest_framework import serializers
from .models import Promotion
from django.contrib.auth.models import User


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'

