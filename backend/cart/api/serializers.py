from rest_framework import serializers
from cart.models import *
from product.models import *
from django.core import serializers as core_serializers
from product.api.serializers import  *

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    total_order = serializers.FloatField(source='get_total_item')
    class Meta:
        model = Order
        fields = ['data_ordered','customer','discount','id','transaction_id','total_order']

class OrderProductSerializer(serializers.ModelSerializer):
    detail = serializers.CharField()
    class Meta:
        model = OrderItem
        fields =  ['price','size','quantity','detail','product','date_added']



