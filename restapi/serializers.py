from rest_framework import serializers
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

from carts.models import Cart
from goods.models import Categories, Products
from users.models import User


class CartSerializer(serializers.ModelSerializer):
    # authentication_classes = (BasicAuthentication, )
    # permissions_classes = (IsAuthenticated, )

    class Meta:
        model = Cart
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # authentication_classes = (BasicAuthentication, )
    # permissions_classes = (IsAuthenticated, )

    class Meta:
        model = User
        fields = '__all__'