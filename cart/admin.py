from django.contrib import admin
from .models import *

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['book_id', 'date_added', 'quantity', 'created_at', 'updated_at']
