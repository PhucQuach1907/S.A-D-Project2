from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'image', 'name', 'author', 'publisher', 'quantity', 'categories', 'price']

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
