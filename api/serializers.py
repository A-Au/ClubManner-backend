from api.models import Products, Users, PantsFitting, ProductCategories, Provinces, ShirtFitting, Size, Styles, Brands, Stores
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'brand', 'price', 'size_data', 'sku', 'category_id')


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ()


class PansFittingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ()


class BrandsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brands
        fields = ('id', 'brand_name')


class ProductCategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategories
        fields = ()


class ProvincesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provinces
        fields = ()


class ShirtFittingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShirtFitting
        fields = ()


class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = ()


class StoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stores
        fields = ()


class StylesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Styles
        fields = ()