from django.conf.urls import url
from main.views import CIndexView


urlpatterns = [
    url(r'^$', CIndexView.as_view(), name='main'),
]
