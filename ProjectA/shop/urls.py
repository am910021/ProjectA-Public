from django.conf.urls import url
from main.views import *


urlpatterns = [
    url(r'^$', CIndexView.as_view(), name='main'),
]
