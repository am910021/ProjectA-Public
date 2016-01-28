from django.conf.urls import url
from shop.views import CShop, BrandView, CategoryView, ItemView


urlpatterns = [
    url(r'^$', CShop.as_view(), name='shop'),
    url(r'^brand/(?P<brandID>[0-9]+)/$', BrandView.as_view(), name='brand'),
    url(r'^category/(?P<categoryID>[0-9]+)/$', CategoryView.as_view(), name='category'),
    url(r'^item/(?P<itemID>[0-9]+)/$', ItemView.as_view(), name='item'),
]
