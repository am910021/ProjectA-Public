from django.conf.urls import url
from pay2go import views
from .views import Pay2go, Test

urlpatterns = [
    #url(r'^pay2go/$', views.pay2go, name='pay2go'),
    url(r'^pay/(?P<groupID>[0-9]+)/$$', Pay2go.as_view(), name='pay'),
    url(r'^NotifyURL/$', views.NotifyURL,name="NotifyURL"),
    url(r'^CustomerURL/$', views.CustomerURL,name="CustomerURL"),
    url(r'^test/(?P<method>1|2+)/$', Test.as_view(), name='test'),
    
    
    #url(r'^TESTNotifyURL$', views.TESTNotifyURL, name='TESTNotifyURL'),
    #url(r'^setting/(?P<status>[\w\-]+)/$', views.SettingView, name='setting'),
]
