from django.conf.urls import url, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductsViewSet)
router.register(r'productcats', views.ProductCategoriesViewSet)
router.register(r'brands', views.BrandsViewSet)
router.register(r'pantsfit', views.PantsFitViewSet)
router.register(r'users', views.UsersViewSet)
router.register(r'provinces', views.ProvincesViewSet)
router.register(r'shirtfit', views.ShirtFitViewSet)
router.register(r'stores', views.StoresViewSet)
router.register(r'styles', views.StylesViewSet)
router.register(r'size', views.SizeViewSet)


urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
