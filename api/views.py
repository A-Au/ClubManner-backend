from django.shortcuts import render
from django.http import HttpResponse
from api.models import Products, Users, PantsFitting, ProductCategories, Provinces, ShirtFitting, Size, Styles, Brands, Stores
from rest_framework import viewsets
from api.serializers import ProductsSerializer, BrandsSerializer, UsersSerializer, PantsFittingSerializer, ProductCategoriesSerializer, ProvincesSerializer, ShirtFittingSerializer, SizeSerializer, StoresSerializer, StylesSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ProductsViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class BrandsViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer


class UsersViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class PantsFitViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = PantsFitting.objects.all()
    serializer_class = PantsFittingSerializer


class ProvincesViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Users.objects.all()
    serializer_class = ProvincesSerializer


class ShirtFitViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Users.objects.all()
    serializer_class = ShirtFittingSerializer


class StoresViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Users.objects.all()
    serializer_class = StoresSerializer


class StylesViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Users.objects.all()
    serializer_class = StylesSerializer


class ProductCategoriesViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Users.objects.all()
    serializer_class = ProductCategoriesSerializer


class SizeViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Users.objects.all()
    serializer_class = SizeSerializer