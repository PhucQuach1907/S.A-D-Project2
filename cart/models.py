from decimal import Decimal

from django.db import models

from book.models import Book
from clothes.models import Clothes
from mobile.models import Mobile


class CartItem(models.Model):
    product_id = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50, default=0)
    type = models.CharField(max_length=50, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cart_items'

    def get_product(self):

        if self.type == 'book':
            try:
                book = Book.objects.using('mongodb').get(id=self.product_id)
                return book
            except Book.DoesNotExist:
                return None
        elif self.type == 'mobile':
            try:
                mobile = Mobile.objects.using('mongodb').get(id=self.product_id)
                return mobile
            except Mobile.DoesNotExist:
                return None
        elif self.type == 'cloth':
            try:
                cloth = Clothes.objects.using('mongodb').get(id=self.product_id)
                return cloth
            except Clothes.DoesNotExist:
                return None

    @property
    def subtotal(self):
        product = self.get_product()
        price_decimal = Decimal(str(product.price))
        return self.quantity * price_decimal

    def __str__(self):
        return self.get_product().name
