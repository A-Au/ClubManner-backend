from django.conf.urls import url, include
from api import views
from rest_framework import routers
from form.views import *
from django.contrib.auth import views as authviews
from form.forms import *

urlpatterns = [
    url(r'^home/$', get_home),
    url(r'^login/$', authviews.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', logout_page),
    url(r'^register/$', register),
    url(r'^details/$', register_details),
    url(r'^success/$', register_success),
]