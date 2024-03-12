from django.contrib import admin
from .models import *


class BaseMongoAdmin(admin.ModelAdmin):
    using = 'mongodb'

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)


@admin.register(Type)
class TypeAdmin(BaseMongoAdmin):
    list_display = ('name', 'description')


@admin.register(Mobile)
class MobileAdmin(BaseMongoAdmin):
    list_display = ('image', 'name', 'producer', 'type', 'quantity', 'price')
    list_display_links = ('name',)
    list_per_page = 5
