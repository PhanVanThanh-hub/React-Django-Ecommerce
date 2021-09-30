from rest_framework import serializers
from product.models import *

class addProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"