from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CartDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model= CartDetail
        fields='__all__'

class CartSerializers(serializers.ModelSerializer):
    cart_detail=CartDetailSerializers(many=True)
    class Meta:
        model= Cart
        fields ='__all__'

class OrderListSerializers(serializers.ModelSerializer):
    class Meta:
        model =Order
        fields ='__all__'

class OrderDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model =Order
        fields ='__all__'

class CreateOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields ='__all__'
        