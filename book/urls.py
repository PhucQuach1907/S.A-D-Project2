from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView, name='home'),
    path('add/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('search/', search_books, name='search_books'),
]
