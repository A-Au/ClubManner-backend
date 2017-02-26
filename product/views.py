from django.shortcuts import render
from django.http import HttpResponse
from product.models import Products
from rest_framework import viewsets
from product.serializers import ProductSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ProductsViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer