from django.db import models
from book.models import Book

class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cart_items'

    @property
    def subtotal(self):
        return self.quantity * self.book.price

    def __str__(self):
        return self.book.name
    
def total():
    cart_items = CartItem.objects.all()
    total = 0
    for item in cart_items:
        total += item.subtotal
    return total
