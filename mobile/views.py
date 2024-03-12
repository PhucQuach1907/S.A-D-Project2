from django.shortcuts import render, redirect
from .models import *
from cart.models import CartItem

def HomeMobileView(request):
    mobiles = Mobile.objects.all().order_by('name')
    return render(request, 'home_mobile.html', {'mobiles': mobiles})

def add_to_cart(request, book_id):
    mobile = Mobile.objects.get(id=book_id)
    if mobile:
        cart_item, created = CartItem.objects.get_or_create(book_id=book_id)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    return redirect('cart_view')
