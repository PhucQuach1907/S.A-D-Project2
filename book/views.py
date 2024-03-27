from django.shortcuts import redirect, render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

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
                type='book',
                user_id=request.user.id
            )
            if not created:
                cart_item.quantity += 1
                cart_item.save()
        return redirect('cart_view')

    @action(detail=False, methods=['post'])
    def create_book(self, request):
        if request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return redirect('home_book')
            return render(request, 'add_product.html', {'form': serializer})
        else:
            return Response({"error": "You don't have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['put'])
    def update_book(self, request, pk=None):
        if request.user.is_superuser:
            book = self.get_object()
            serializer = self.get_serializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return redirect('home_book')
            return render(request, 'home_book.html', {'form': serializer})
        else:
            return Response({"error": "You don't have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['delete'])
    def delete_book(self, request, pk=None):
        if request.user.is_superuser:
            book = self.get_object()
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "You don't have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)
