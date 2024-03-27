from rest_framework import serializers

from .models import Mobile


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ['id', 'image', 'name', 'producer', 'type', 'quantity', 'price']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0")
        return value

    def validate_price(self, value):
        try:
            float(value)
        except ValueError:
            raise serializers.ValidationError("Price must be a number.")
        return value
