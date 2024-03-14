from rest_framework import serializers

from .models import CartItem


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'type', 'date_added', 'quantity', 'created_at', 'updated_at', 'subtotal']
