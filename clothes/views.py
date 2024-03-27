from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=False, methods=['post'])
    def create_cloth(self, request):
        if request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return redirect('home_clothes')
            return render(request, 'add_product.html', {'form': serializer})
        else:
            return Response({"error": "You don't have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)