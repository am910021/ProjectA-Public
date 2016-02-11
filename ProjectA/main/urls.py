from django.conf.urls import url
from main.views import IndexView, NoticeView, NoticeDetial, Deals


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='main'),
    url(r'^notice/$', NoticeView.as_view(), name='notice'),
    url(r'^notice/detail/(?P<noticeID>[0-9]+)/$', NoticeDetial.as_view(), name='noticeDetail'),
    url(r'^deals/$', Deals.as_view(), name='deals'),

]
