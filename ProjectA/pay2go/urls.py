from django.conf.urls import url
from pay2go import views
from .views import Pay2go

urlpatterns = [
    url(r'^pay/(?P<groupID>[0-9]+)/$$', Pay2go.as_view(), name='pay'),
    url(r'^NotifyURL/$', views.NotifyURL,name="NotifyURL"),
    url(r'^CustomerURL/$', views.CustomerURL,name="CustomerURL"),
]
