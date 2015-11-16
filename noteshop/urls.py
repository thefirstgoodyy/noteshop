"""noteshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from noteshop import settings
from person import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup$', views.newUser, name='signup'),
    url(r'^create$', views.create_user, name='createuser'),
    url(r'^signin$', views.authentication, name='signin'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^', include('product.urls', namespace='Products',
                      app_name='Products')),
    url(r'^basket/', include('basket.urls', namespace='basket',
                             app_name='basket')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
