from rest_framework import serializers

from .models import *


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'product_name',
            'price',
            'quantity',
        ]