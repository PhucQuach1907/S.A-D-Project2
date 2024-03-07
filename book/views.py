from django.shortcuts import render, redirect
from .models import Book
from cart.models import CartItem

def HomeView(request):
    books = Book.objects.all().order_by('name')
    return render(request, 'home.html', {'books': books})

def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    if book:
        cart_item, created = CartItem.objects.get_or_create(book_id=book_id)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    return redirect('cart_view')
