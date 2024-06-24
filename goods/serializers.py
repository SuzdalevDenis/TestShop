from rest_framework import serializers

from goods.models import Categories, Products


# class ProductSerializer(serializers.ModelSerializer):
#
#     def create(self, validated_data):
#         return Products.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.user = validated_data.get('user', instance.user)
#         instance.product = validated_data.get('product', instance.product)
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.created_timestamp = validated_data.get('created_timestamp', instance.created_timestamp)
#         instance.save()
#         return instance
#
#     class Meta:
#         model = Products
#         fields = '__all__'


# class CategorySerializer(serializers.ModelSerializer):
#
#     def create(self, validated_data):
#         return Categories.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.user = validated_data.get('user', instance.user)
#         instance.product = validated_data.get('product', instance.product)
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.created_timestamp = validated_data.get('created_timestamp', instance.created_timestamp)
#         instance.save()
#         return instance
#
#     class Meta:
#         model = Categories
#         fields = '__all__'

