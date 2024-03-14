from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.decorators import action

from cart.models import CartItem
from .serializers import *


class MobileViewAPI(viewsets.ModelViewSet):
    queryset = Mobile.objects.all().order_by('name')
    serializer_class = MobileSerializer

    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, pk=None):
        mobile = self.get_object()
        if mobile:
            cart_item, created = CartItem.objects.get_or_create(
                product_id=mobile.id,
                type='mobile'
            )
            if not created:
                cart_item.quantity += 1
                cart_item.save()
        return redirect('cart_view')
