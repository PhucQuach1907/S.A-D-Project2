from django.contrib import admin

from .models import *


# Register your models here.
class BaseMongoAdmin(admin.ModelAdmin):
    using = 'mongodb'

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)


@admin.register(Type)
class TypeAdmin(BaseMongoAdmin):
    list_display = ('name',)


@admin.register(Clothes)
class ClothesAdmin(BaseMongoAdmin):
    list_display = ('image', 'name', 'type', 'brand_name', 'quantity', 'price')
