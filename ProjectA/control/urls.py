from django.conf.urls import url
from django.views.generic.base import RedirectView
from control.views import CAdminIndex, redirectAdminIndex, CAdminSignIn
from .views import VConfig, ConfigEmail, ConfigPay2Go, ConfigKey
from .views import CBrand, CBrandAdd, CBrandEdit, CBrandPreview
from .views import CCategory, CCategoryAdd, CCategoryEdit
from .views import ItemManage, ItemAdd, ItemEdit, ItemPreview
from .views import OrderView, NoticePost, NoticeView


urlpatterns = [
    url(r'^$', CAdminIndex.as_view(), name='admin'),
    url(r'^admin/login/$', CAdminSignIn.as_view(), name='SignIn'),
    url(r'^config/$', VConfig.as_view(), name='config'),
    url(r'^config/email/$', ConfigEmail.as_view(), name='configEmail'),
    url(r'^config/pay2go/$', ConfigPay2Go.as_view(), name='configPay2go'),
    url(r'^config/key/$', ConfigKey.as_view(), name='configKey'),
    
    url(r'^notice/$', NoticeView.as_view(),name="notice"),
    url(r'^notice/post/$', NoticePost.as_view(),name="noticePost"),
    
    url(r'^brand/$', CBrand.as_view(), name='brand'),
    url(r'^brandadd/$', CBrandAdd.as_view(), name='brandAdd'),
    url(r'^brandedit/(?P<brandID>[0-9]+)/$', CBrandEdit.as_view(), name='brandEdit'),
    url(r'^brand/preview/(?P<brandID>[0-9]+)/$', CBrandPreview.as_view(), name='brandPreview'),
    
    url(r'^category/$', CCategory.as_view(), name='category'),
    url(r'^categoryadd/$', CCategoryAdd.as_view(), name='categoryAdd'),
    url(r'^categoryedit/(?P<categoryID>[0-9]+)/$', CCategoryEdit.as_view(), name='categoryEdit'),
    
    url(r'^item/$', ItemManage.as_view(), name='item'),
    url(r'^item/add/$', ItemAdd.as_view(), name='itemAdd'),
    url(r'^item/edit/(?P<itemID>[0-9]+)/$', ItemEdit.as_view(), name='itemEdit'),
    url(r'^item/brand/(?P<brandID>[0-9]+)/$', ItemEdit.as_view(), name='itemBrand'),
    url(r'^item/category/(?P<categoryID>[0-9]+)/$', ItemEdit.as_view(), name='itemCategory'),
    url(r'^item/preview/(?P<itemID>[0-9]+)/$', ItemPreview.as_view(), name='itemPreview'),
    
    url(r'^order/$', OrderView.as_view(), name='orderNone'),
    url(r'^order/(?P<status>[0-9]+)/$', OrderView.as_view(), name='order'),

    url(r'^.*$', redirectAdminIndex),
]
