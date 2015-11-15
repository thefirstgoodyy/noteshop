from django.conf.urls import url
from Product import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shop/(?P<label>\d+)/notebooks/$',
        views.show_notebooks,
        name="notebooks"),
    ]
