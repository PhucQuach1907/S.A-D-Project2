from rest_framework import serializers

from .models import Mobile


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ['id', 'image', 'name', 'producer', 'type', 'quantity', 'price']
