from django.shortcuts import render
from django.http import HttpResponse
from model.models import Product, Profile, PantsFitting, ProductCategory, Province, ShirtFitting, Size, Style, Brand, Store
from rest_framework import viewsets
from api.serializers import ProductSerializer, BrandSerializer, ProfileSerializer, PantsFittingSerializer, ProductCategorySerializer, ProvinceSerializer, ShirtFittingSerializer, SizeSerializer, StoreSerializer, StyleSerializer


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


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


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
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class ShirtFitViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = ShirtFitting.objects.all()
    serializer_class = ShirtFittingSerializer


class StoreViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StyleViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class SizeViewSet(viewsets.ModelViewSet):
    """
    API Endpoint
    """
    queryset = Size.objects.all()
    serializer_class = SizeSerializer



'''def get_signup(request):
    if request.method == 'POST':
        signupForm = SignupForm(request.POST)

        if signupForm.is_valid():
            signupForm.save()

            return HttpResponseRedirect('/REPLACE WITH A LEGIT PATH')
    else:
        signupForm = SignupForm()

    return render(request, 'signup.html', {'form': signupForm})

def get_userUpdate(request):
    if request.method == 'POST':
        userUpdateForm = ProfileUpdateForm(request.POST)

        if userUpdateForm:
            userUpdateForm.save()

            return HttpResponseRedirect('')

    else:
        userUpdateForm = ProfileUpdateForm()

    return render(request, 'profile.html', {'form': userUpdateForm})'''