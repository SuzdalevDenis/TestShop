from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'restapi'

router1 = routers.DefaultRouter()
router1.register(
    r'Cart', views.CartViewSet, basename='Cart',
),

router2 = routers.DefaultRouter()
router2.register(
    r'Categories', views.CartViewSet, basename='Categories',
),

router = (router1, router2)

urlpatterns = [
    path('', include(router.urls)),
    path('rest_api/', include('rest_framework.urls', namespace='rest_framework')),
]

#'api/v1/cartlist/', views.CartViewSet
