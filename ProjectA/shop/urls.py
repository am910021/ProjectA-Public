from django.conf.urls import url
from shop.views import CShop


urlpatterns = [
    url(r'^$', CShop.as_view(), name='shop'),
]
