from main.views import BaseView
from shop.models import Type, Item
from django.contrib.auth.models import User
from account.models import UserProfile

class CShop(BaseView):
    template_name = 'shop/detail.html'
    page_title = '商店'
    
    def get(self, request, *args, **kwargs):
        item = Item.objects.filter(type=1)
        print("aaaaaaaaaaaaaaaaaaa")
        for i in item:
            print(i.name)
            print(i.type.getValue())
        
        user = UserProfile.objects.get(user=2)
        print("bbbbbbbbbbbbbbb")
        print(user.fullName)
        print(user.user)
        
        kwargs['find'] = True
        return BaseView.get(self, request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super(CShop, self).post(request, *args, **kwargs)