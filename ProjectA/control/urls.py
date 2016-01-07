from django.conf.urls import url
from control.views import CAdminIndex, CAdminSignIn, CBrand, CBrandAdd, CBrandEdit, CBrandPreview


urlpatterns = [
    url(r'^$', CAdminIndex.as_view(), name='admin'),
    url(r'^admin/login/$', CAdminSignIn.as_view(), name='SignIn'),
    
    url(r'^brand/$', CBrand.as_view(), name='brand'),
    url(r'^brandadd/$', CBrandAdd.as_view(), name='brandAdd'),
    url(r'^brandedit/(?P<brandID>[0-9]+)/$', CBrandEdit.as_view(), name='brandEdit'),
    url(r'^brand/preview/(?P<brandID>[0-9]+)/$', CBrandPreview.as_view(), name='brandPreview'),
    
    url(r'^category/$', CBrand.as_view(), name='category'),
    url(r'^categoryadd/$', CBrand.as_view(), name='categoryAdd'),
    url(r'^categoryedit/$', CBrand.as_view(), name='categoryEdit'),
]
