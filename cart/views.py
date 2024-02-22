from django.shortcuts import render
from .models import CartItem

# Create your views here.
def cart_view(request):
    cart_items = CartItem.objects.all()
    return render(request, 'cart.html', {'cart_items': cart_items})
