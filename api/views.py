from django.shortcuts import render
from django.http import HttpResponse
from api.models import Product, User, PantsFitting, ProductCategory, Province, ShirtFitting, Size, Style, Brand, Store
from rest_framework import viewsets
from api.serializers import ProductSerializer, BrandSerializer, UserSerializer, PantsFittingSerializer, ProductCategorySerializer, ProvinceSerializer, ShirtFittingSerializer, SizeSerializer, StoreSerializer, StyleSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BrandViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PantsFitViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = PantsFitting.objects.all()
    serializer_class = PantsFittingSerializer


class ProvinceViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = User.objects.all()
    serializer_class = ProvinceSerializer


class ShirtFitViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = User.objects.all()
    serializer_class = ShirtFittingSerializer


class StoreViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = User.objects.all()
    serializer_class = StoreSerializer


class StyleViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = User.objects.all()
    serializer_class = StyleSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = User.objects.all()
    serializer_class = ProductCategorySerializer


class SizeViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = User.objects.all()
    serializer_class = SizeSerializer