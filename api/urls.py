from django.conf.urls import url, include
from api import views
from rest_framework import routers
from .views import *
from django.contrib.auth import views as authviews
from .forms import LoginForm


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'productcats', views.ProductCategoryViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'pantsfit', views.PantsFitViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'provinces', views.ProvinceViewSet)
router.register(r'shirtfit', views.ShirtFitViewSet)
router.register(r'stores', views.StoreViewSet)
router.register(r'styles', views.StyleViewSet)
router.register(r'size', views.SizeViewSet)


urlpatterns = [
    url(r'^login/$', authviews.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^$', home),
    url(r'^logout/$', logout_page),
    url(r'^register/$', register),
    url(r'details/$', register_details),
    url(r'^success/$', register_success),
    url(r'^home/$', home),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
