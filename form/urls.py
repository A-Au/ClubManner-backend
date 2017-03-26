from django.conf.urls import url, include
from api import views
from rest_framework import routers
from .views import *
from django.contrib.auth import views as authviews
from .forms import *

urlpatterns = {
    url(r'^login/$', authviews.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^home$', home),
    url(r'^logout/$', logout_page),
    url(r'^register/$', register),
    url(r'^details/$', register_details),
    url(r'^success/$', register_success),
    url(r'^home/$', home),
}