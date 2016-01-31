from django.conf.urls import url
from pay2go import views

urlpatterns = [
    url(r'^pay2go/$', views.pay2go, name='pay2go'),
    url(r'^NotifyURL/$', views.NotifyURL,name="NotifyURL"),
    url(r'^CustomerURL/$', views.CustomerURL),
    #url(r'^TESTNotifyURL$', views.TESTNotifyURL, name='TESTNotifyURL'),
    #url(r'^setting/(?P<status>[\w\-]+)/$', views.SettingView, name='setting'),
]
