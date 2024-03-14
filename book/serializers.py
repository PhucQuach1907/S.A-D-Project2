from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'image', 'name', 'author', 'publisher', 'quantity', 'categories', 'price']
