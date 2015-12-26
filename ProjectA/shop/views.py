from main.views import BaseView
from shop.models import Type, Item


class CShop(BaseView):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(type="a")
        return BaseView.get(self, request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super(CShop, self).post(request, *args, **kwargs)