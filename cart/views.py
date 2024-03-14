from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from .models import CartItem
from .serializers import CartSerializer


# Create your views here.
class CartViewAPI(viewsets.ModelViewSet):
    queryset = CartItem.objects.all().order_by('date_added')
    serializer_class = CartSerializer

    @action(detail=True, methods=['delete'])
    def remove_from_cart(self, request, pk=None):
        cart_item = get_object_or_404(CartItem, pk=pk)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
