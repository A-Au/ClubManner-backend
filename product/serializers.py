from product.models import Products
from rest_framework import serializers

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'brand')