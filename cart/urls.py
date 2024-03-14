from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='cart.html'), name='cart_view'),
    path('remove/<int:pk>/', CartViewAPI.as_view({'delete': 'remove_from_cart'}), name='remove-from-cart'),
]
