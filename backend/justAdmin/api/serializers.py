from rest_framework import serializers
from product.models import *
from django.contrib.auth.models import User
from register.models import *
from justAdmin.models import  *

from cart.models import *
class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CustomerSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class IncomeSeriaLizer(serializers.ModelSerializer):
    total_profit = serializers.FloatField()
    class Meta:
        model = Income
        fields = "__all__"
        extra_fields = ['total_profit']

class OrderLast7DaySeriaLizer(serializers.ModelSerializer):
    total_order = serializers.FloatField(source='get_total_item')
    class Meta:
        model = Order
        fields = "__all__"
        extra_fields= ['total_order']


class BillLast7DaySeriaLizer(serializers.ModelSerializer):
    nameProduct = serializers.CharField()
    class Meta:
        model = Bill
        fields = "__all__"
        extra_fields = ['nameProduct']

