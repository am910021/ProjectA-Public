from django.conf.urls import url
from shop.views import CShop, dropbox_auth_start, dropbox_auth_finish


urlpatterns = [
    url(r'^$', CShop.as_view(), name='shop'),
    url(r'^dropbox_auth_start/?$',dropbox_auth_start),
    url(r'^dropbox_auth_finish/?$',dropbox_auth_finish),
]
