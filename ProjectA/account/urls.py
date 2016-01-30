from django.conf.urls import url
from account.views import CSignUp, CSignIn, CSignOut, CenterView, CProfile, MyCartView, CheckOutView
from .views import removeItem


urlpatterns = [
    url(r'^signup/$', CSignUp.as_view(), name='signup'),
    url(r'^signin/$', CSignIn.as_view(), name='signin'),
    url(r'^signout/$', CSignOut.as_view(), name='signout'),
    url(r'^center/$', CenterView.as_view(), name='center'),
    url(r'^profile/$', CProfile.as_view(), name='profile'),
    url(r'^mycart/$', MyCartView.as_view(), name='mycart'),
    url(r'^removeitem/$', removeItem, name='removeItem'),
    url(r'^checkout/$', CheckOutView.as_view(), name='checkout'),
]
