from django.conf.urls import url, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'productcats', views.ProductCategoryViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'pantsfit', views.PantsFitViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'provinces', views.ProvinceViewSet)
router.register(r'shirtfit', views.ShirtFitViewSet)
router.register(r'stores', views.StoreViewSet)
router.register(r'styles', views.StyleViewSet)
router.register(r'size', views.SizeViewSet)


urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
