from django.db import models
from book.models import Book

class CartItem(models.Model):
    book_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cart_items'

    def get_book(self):
        try:
            book = Book.objects.using('mongodb').get(id=self.book_id)
            return book
        except Book.DoesNotExist:
            return None
        
    def price(self):
        return self.get_book.price

    @property
    def subtotal(self):
        return self.quantity * self.get_book.price

    def __str__(self):
        return self.get_book.name
    
def total():
    cart_items = CartItem.objects.all()
    total = 0
    for item in cart_items:
        total += item.subtotal
    return total
