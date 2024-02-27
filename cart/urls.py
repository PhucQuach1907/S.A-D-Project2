from django.urls import path
from .views import *

urlpatterns = [
    path('', cart_view, name='cart_view'),
    path('delete/<int:book_id>/', remove_from_cart, name='remove_from_cart'),
]
