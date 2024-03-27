from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='home_book.html'), name='home_book'),
    path('books/add-to-cart/<int:pk>/', BookViewAPI.as_view({'post': 'add_to_cart'}), name='add-to-cart'),
    path('books/add/', BookViewAPI.as_view({'post': 'create_book'}), name='create_book'),
    path('books/update/<int:pk>/', BookViewAPI.as_view({'put': 'update_book'}), name='update_book'),
]
