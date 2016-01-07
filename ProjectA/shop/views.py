from main.views import BaseView
from shop.models import Type, Item
from django.contrib.auth.models import User
from account.models import UserProfile
#from django.http import HttpResponseRedirect, HttpResponseForbidden,HttpResponse

class CShop(BaseView):
    template_name = 'shop/detail.html'
    page_title = '商店'
    
    def get(self, request, *args, **kwargs):
        kwargs['find'] = True
        return super(CShop, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super(CShop, self).post(request, *args, **kwargs)