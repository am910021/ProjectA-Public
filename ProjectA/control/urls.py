from django.conf.urls import url
from control.views import CAdminIndex, CAdminSignIn


urlpatterns = [
    url(r'^$', CAdminIndex.as_view(), name='admin'),
    url(r'^admin/login/$', CAdminSignIn.as_view(), name='SignIn'),
]
