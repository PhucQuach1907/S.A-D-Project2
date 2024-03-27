from django.shortcuts import redirect, render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=False, methods=['post'])
    def create_mobile(self, request):
        if request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return redirect('home_mobile')
            return render(request, 'add_product.html', {'form': serializer})
        else:
            return Response({"error": "You don't have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)
