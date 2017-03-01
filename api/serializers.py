from api.models import Products, Users, PantsFitting, ProductCategories, Provinces, ShirtFitting, Size, Styles, Brands, Stores
from rest_framework import serializers


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'brand', 'price', 'size_data', 'sku', 'category_id')


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
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


class BrandsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brands
        fields = ('id', 'brand_name')


class ProductCategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategories
        fields = ('id', 'category_name')


class ProvincesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provinces
        fields = ('id', 'province_name')


class ShirtFittingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShirtFitting
        fields = ('id', 'sfit_name')


class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'size_name')


class StoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stores
        fields = ('id', 'store_name')


class StylesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Styles
        fields = ('id', 'style_name')