from django.conf.urls import url, include
from product import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'get', views.ProductsViewSet)

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
