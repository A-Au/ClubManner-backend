from api.models import Product, User, PantsFitting, ProductCategory, Province, ShirtFitting, Size, Style, Brand, Store
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'brand', 'price', 'size_data', 'sku', 'category_id')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 
            'last_name', 
            'password', 
            'email', 
            'phone', 
            'address',
            'postal_code',
            'city',
            'province',
            'country',
            'birth_month',
            'birth_day',
            'birth_year',
            'pants_fit',
            'shirt_fit',
            'shirt_size',
            'pants_size',
            'shirt_min_price',
            'shirt_max_price',
            'pants_min_price',
            'pants_max_price',
            'shoes_min_price',
            'shoes_max_price',
            'acces_min_price',
            'acces_max_price',
            'style_pref',
            'store_pref',
            'price_min',
            'price_max',
            'referral')


class PantsFittingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PantsFitting
        fields = ('id', 'pfit_name')


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'brand_name')


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'category_name')


class ProvinceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Province
        fields = ('id', 'province_name')


class ShirtFittingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShirtFitting
        fields = ('id', 'sfit_name')


class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'size_name')


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'store_name')


class StyleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Style
        fields = ('id', 'style_name')