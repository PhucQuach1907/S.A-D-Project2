from rest_framework import serializers

from .models import Clothes


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ['id', 'image', 'name', 'brand_name', 'type', 'quantity', 'price']
