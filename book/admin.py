from django.contrib import admin
from .models import *

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'author', 'publisher', 'price']
    raw_id_fields = ['categories']
