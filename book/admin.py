from django.contrib import admin

from .forms import BookAdminForm
from .models import *


class BaseMongoAdmin(admin.ModelAdmin):
    using = 'mongodb'

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)


@admin.register(Category)
class CategoryAdmin(BaseMongoAdmin):
    list_display = ('name', 'description')


@admin.register(Book)
class BookAdmin(BaseMongoAdmin):
    form = BookAdminForm
    list_display = ('image', 'name', 'quantity', 'author', 'publisher', 'price')
    list_display_links = ('name',)
    list_per_page = 50
    list_filter = ('author', 'publisher', 'categories')
    search_fields = ('name', 'author__name', 'publisher__name')

    fieldsets = (
        (None, {
            'fields': ('image', 'name', 'quantity', 'price')
        }),
        ('Categorization', {
            'fields': ('categories',)
        }),
        ('Associations', {
            'fields': ('author', 'publisher')
        }),
    )
