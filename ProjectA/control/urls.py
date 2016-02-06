from django.conf.urls import url
from django.views.generic.base import RedirectView
from control.views import CAdminIndex, redirectAdminIndex, CAdminSignIn, VConfig, ConfigEmail, ConfigPay2Go
from .views import CBrand, CBrandAdd, CBrandEdit, CBrandPreview
from .views import CCategory, CCategoryAdd, CCategoryEdit
from .views import ItemManage, ItemAdd, ItemEdit, ItemPreview


urlpatterns = [
    url(r'^$', CAdminIndex.as_view(), name='admin'),
    url(r'^admin/login/$', CAdminSignIn.as_view(), name='SignIn'),
    url(r'^config/$', VConfig.as_view(), name='config'),
    url(r'^config/email/$', ConfigEmail.as_view(), name='configEmail'),
    url(r'^config/pay2go/$', ConfigPay2Go.as_view(), name='configPay2go'),
    
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
    url(r'^item/preview/(?P<itemID>[0-9]+)/$', ItemPreview.as_view(), name='itemPreview'),
    
    url(r'^order/(?P<groupID>[0-9]+)/$', ItemManage.as_view(), name='group'),

    url(r'^.*$', redirectAdminIndex),
]
