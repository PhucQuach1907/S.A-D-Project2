from django.contrib import admin

from .models import *


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'type', 'date_added', 'quantity', 'created_at', 'updated_at']
