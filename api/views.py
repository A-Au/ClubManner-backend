from django.shortcuts import render
from django.http import HttpResponse
from api.models import Products, Users, PantsFitting, ProductCategories, Provinces, ShirtFitting, Size, Styles, Brands, Stores
from rest_framework import viewsets
from api.serializers import ProductSerializer, BrandsSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ProductsViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class BrandsViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
