from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from .models import CartItem
from book.models import Book

# Create your views here.
def cart_view(request):
    cart_items = CartItem.objects.all()

    total_price = 0
    for item in cart_items:
        total_price += item.subtotal

    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total_price})

def remove_from_cart(request, book_id):
    item = get_object_or_404(CartItem, book_id=book_id)
    
    item.delete()
    
    return redirect('cart_view')
    
