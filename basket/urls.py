from django.conf.urls import url
from basket import views

urlpatterns = [
    url(r'^$', views.showBasket, name="show"),
    url(r'^addProduct/(?P<product_id>\d+)/$', views.addItemToBasket,
        name="add"),
    url(r'^deleterow/(?P<item_id>\d+)/$', views.deleteRow, name="deleteRow")
]
