from api.models import Product, Profile, PantsFitting, ProductCategory, Province, ShirtFitting, Size, Style, Brand, Store
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 
                  'name', 
                  'brand', 
                  'price', 
                  'size_data', 
                  'sku', 
                  'category_id')


class ProfileSerializer(serializers.ModelSerializer):
    #province = serializers.StringRelatedField(many=False)
    class Meta:
        model = Profile
        fields = ('user',
            'address',
            'postal_code',
            'city',
            'province',
            'country',
            'birthday',
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


class PantsFittingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantsFitting
        fields = ('id', 'pfit_name')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'brand_name')


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'category_name')


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id', 'province_name')


class ShirtFittingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShirtFitting
        fields = ('id', 'sfit_name')


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'size_name')


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'store_name')


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ('id', 'style_name')