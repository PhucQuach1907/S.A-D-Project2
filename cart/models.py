from decimal import Decimal
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

    @property
    def subtotal(self):
        book = self.get_book()
        price_decimal = Decimal(str(book.price))
        return self.quantity * price_decimal

    def __str__(self):
        return self.get_book.name
