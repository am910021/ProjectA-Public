from django.conf.urls import url
from account.views import CSignUp, CSignIn, CSignOut, CMy, CProfile


urlpatterns = [
    url(r'^signup$', CSignUp.as_view(), name='signup'),
    url(r'^signin$', CSignIn.as_view(), name='signin'),
    url(r'^signout$', CSignOut.as_view(), name='signout'),
    url(r'^my$', CMy.as_view(), name='myaccount'),
    url(r'^profile$', CProfile.as_view(), name='profile'),
]
