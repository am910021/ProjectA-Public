from django.conf.urls import url
from account.views import CSignUp, CSignIn, CSignOut, CenterView, CProfile, MyCartView
from .views import  CheckOut, Agreement, Verification, VerificationEemail
from .views import removeItem, ForgetView, ForgetReset, OrderDetailView, OrderView


urlpatterns = [
    url(r'^signup/$', CSignUp.as_view(), name='signup'),
    url(r'^signin/$', CSignIn.as_view(), name='signin'),
    url(r'^signout/$', CSignOut.as_view(), name='signout'),
    url(r'^forget/$', ForgetView.as_view(), name='forget'),
    url(r'^forget/reset/(?P<base64string>.+)$', ForgetReset.as_view(), name='forgetReset'),
    url(r'^center/$', CenterView.as_view(), name='center'),
    url(r'^profile/$', CProfile.as_view(), name='profile'),
    url(r'^mycart/$', MyCartView.as_view(), name='mycart'),
    
    url(r'^order/$', OrderView.as_view(), name='order'),
    url(r'^order/detail/(?P<method>checkout|list+)/(?P<groupID>[0-9]+)/$', OrderDetailView.as_view(), name='orderDetail'),
    
    url(r'^removeitem/$', removeItem, name='removeItem'),
    url(r'^verify/$', Verification.as_view(), name='verify'),
    url(r'^verify/email/(?P<base64string>.+)$', VerificationEemail.as_view(), name='verifyEmail'),
    
    url(r'^checkout/agreement/$', Agreement.as_view(), name='agreement'),
    url(r'^checkout/$', CheckOut.as_view(), name='checkout'),
]
