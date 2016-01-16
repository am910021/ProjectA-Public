from django.conf.urls import url
from control.views import CAdminIndex, CAdminSignIn, VConfig, ConfigEmail
from .views import CBrand, CBrandAdd, CBrandEdit, CBrandPreview
from .views import CCategory, CCategoryAdd, CCategoryEdit
from .views import Item, ItemAdd, ItemEdit


urlpatterns = [
    url(r'^$', CAdminIndex.as_view(), name='admin'),
    url(r'^admin/login/$', CAdminSignIn.as_view(), name='SignIn'),
    url(r'^config/$', VConfig.as_view(), name='config'),
    url(r'^config/email/$', ConfigEmail.as_view(), name='configEmail'),
    
    
    url(r'^brand/$', CBrand.as_view(), name='brand'),
    url(r'^brandadd/$', CBrandAdd.as_view(), name='brandAdd'),
    url(r'^brandedit/(?P<brandID>[0-9]+)/$', CBrandEdit.as_view(), name='brandEdit'),
    url(r'^brand/preview/(?P<brandID>[0-9]+)/$', CBrandPreview.as_view(), name='brandPreview'),
    
    url(r'^category/$', CCategory.as_view(), name='category'),
    url(r'^categoryadd/$', CCategoryAdd.as_view(), name='categoryAdd'),
    url(r'^categoryedit/(?P<categoryID>[0-9]+)/$', CCategoryEdit.as_view(), name='categoryEdit'),
    
    url(r'^item/$', Item.as_view(), name='item'),
    url(r'^item/add/$', ItemAdd.as_view(), name='itemAdd'),
    url(r'^item/edit/(?P<brandID>[0-9]+)/$', ItemEdit.as_view(), name='itemEdit'),
]
