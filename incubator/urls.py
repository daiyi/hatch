from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<username>[a-z0-9]+)/?$', views.incubator),
    url(r'^$', views.incubator, {'username': ''}, name='home'),
]
