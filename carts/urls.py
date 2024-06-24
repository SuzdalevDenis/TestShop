from django.urls import path, include
from rest_framework import routers

from carts import views

# from .views import CartViewSet

app_name = 'carts'

# router = routers.DefaultRouter()
# router.register(
#     r'Cart', views.CartViewSet, basename='Cart'
# )


urlpatterns = [
    # path('', include(router.urls)),
    path('cart_add/', views.cart_add, name='cart_add'),
    path('cart_change/', views.cart_change, name='cart_change'),
    path('cart_remove/', views.cart_remove, name='cart_remove'),
    # path('rest_api/', include('rest_framework.urls', namespace='rest_framework')),
]
