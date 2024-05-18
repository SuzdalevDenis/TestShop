from rest_framework import serializers

from carts.models import Cart


class CartSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cart
        fields = ('user', 'product', 'quantity', 'created_timestamp')
