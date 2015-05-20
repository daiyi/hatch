from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/(?P<param>[a-z]+)/?$', views.api, name='api'),
    url(r'^(?P<username>[a-z0-9]+)/?$', views.incubator, name='user'),
    url(r'^$', views.incubator, {'username': ''}, name='home'),
]
