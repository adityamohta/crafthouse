from django.conf.urls import url
from .views import (
    home,
    product_detail,
    about,
    contact,
    product_list
)

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^products/$', product_list, name="product_list"),
    url(r'^about/$', about, name="about"),
    url(r'^contact/$', contact, name="contact"),
    url(r'^products/(?P<id>\d+)/$', product_detail, name="product_detail"),
]
