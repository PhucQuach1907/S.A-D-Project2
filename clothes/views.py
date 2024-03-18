from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import action

from cart.models import CartItem
from .serializers import *


# Create your views here.
class ClothesViewAPI(viewsets.ModelViewSet):
    queryset = Clothes.objects.all().order_by('name')
    serializer_class = ClothesSerializer

    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, pk=None):
        cloth = self.get_object()
        if cloth:
            cart_item, created = CartItem.objects.get_or_create(
                product_id=cloth.id,
                type='cloth'
            )
            if not created:
                cart_item.quantity += 1
                cart_item.save()
        return redirect('cart_view')
