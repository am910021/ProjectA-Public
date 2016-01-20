from django.conf.urls import url
from shop.views import CShop, BrandView


urlpatterns = [
    url(r'^$', CShop.as_view(), name='shop'),
    url(r'^brand/(?P<brandID>[0-9]+)/$', BrandView.as_view(), name='brand'),
    url(r'^category/(?P<categoryID>[0-9]+)/$', BrandView.as_view(), name='category'),

]
