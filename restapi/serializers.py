from rest_framework import serializers

from carts.models import Cart
from goods.models import Categories, Products


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ('user', 'product', 'quantity', 'created_timestamp')


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ('name', 'slug')


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ('name', 'slug', 'description', 'quantity', 'category')

