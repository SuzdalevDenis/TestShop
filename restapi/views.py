from django.shortcuts import render
from rest_framework import viewsets, generics

from .serializers import CartSerializer, CategoriesSerializer, ProductsSerializer

from carts.models import Cart
from goods.models import Categories, Products


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all().order_by('name')
    serializer_class = CategoriesSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductsSerializer
