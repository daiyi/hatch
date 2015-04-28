from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^$', 'hatch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('incubator.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    # django-user-accounts
    url(r"^account/", include("account.urls")),

    # python-social-auth
    url('', include('social.apps.django_app.urls', namespace='social'))
]
