from django.conf.urls import url
from control.views import CAdminIndex


urlpatterns = [
    url(r'^$', CAdminIndex.as_view(), name='admin'),
]
