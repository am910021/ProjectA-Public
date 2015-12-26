from django.conf.urls import url
from account.views import CSignUp, CSignIn, CSignOut


urlpatterns = [
    url(r'^signup$', CSignUp.as_view(), name='SignUp'),
    url(r'^signin$', CSignIn.as_view(), name='SignIn'),
    url(r'^signout$', CSignOut.as_view(), name='SignOut'),
]
