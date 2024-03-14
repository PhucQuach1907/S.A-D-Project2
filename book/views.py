from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.decorators import action

from cart.models import CartItem
from .serializers import *


class BookViewAPI(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, pk=None):
        book = self.get_object()
        if book:
            cart_item, created = CartItem.objects.get_or_create(
                product_id=book.id,
                type='book'
            )
            if not created:
                cart_item.quantity += 1
                cart_item.save()
        return redirect('cart_view')
