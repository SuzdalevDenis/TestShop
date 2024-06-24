from django.shortcuts import render
from rest_framework import viewsets, generics

from .serializers import CartSerializer, CategorySerializer, ProductSerializer, UserSerializer

from carts.models import Cart
from goods.models import Categories, Products
from users.models import User


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all().order_by('id')
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


# class CartListView(generics.ListAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#
#
# class ProductListView(generics.ListAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#
#
# class CategoryListView(generics.ListAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategorySerializer
#
#
# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class CartDetailView(generics.RetrieveAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#
#
# class ProductDetailView(generics.RetrieveAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#
#
# class CategoryDetailView(generics.RetrieveAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategorySerializer
#
#
# class UserDetailView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
