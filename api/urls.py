from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book.views import *
from mobile.views import *
from cart.views import *
from search.views import *
from clothes.views import *

router = DefaultRouter()
router.register(r'books', BookViewAPI)
router.register(r'mobiles', MobileViewAPI)
router.register(r'cart-items', CartViewAPI)
router.register(r'clothes', ClothesViewAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', SearchAPI.as_view(), name='search'),
    path('search-image/', SearchImageAPI.as_view(), name='search_image'),
    path('search-voice/', SearchByVoiceAPI.as_view(), name='search_voice')
]
