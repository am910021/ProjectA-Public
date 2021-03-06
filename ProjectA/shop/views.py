from main.views import BaseView
from shop.models import Item, Brand, Category
from django.contrib.auth.models import User
from account.models import Profile
#from django.http import HttpResponseRedirect, HttpResponseForbidden,HttpResponse

class CShop(BaseView):
    template_name = 'shop/detail.html'
    page_title = '商店'
    
    def get(self, request, *args, **kwargs):
        kwargs['find'] = True
        return super(CShop, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super(CShop, self).post(request, *args, **kwargs)
    
class BrandView(BaseView):
    template_name = 'shop/brand.html' # xxxx/xxx.html
    page_title = '' # title

    def get(self, request, *args, **kwargs):
        if "brandID" in kwargs:
            try:
                brand = Brand.objects.get(id=kwargs['brandID'])
                category = Category.objects.filter(brand=brand)
                self.page_title = brand.name
                kwargs['category'] = category
                kwargs['brand'] = brand
            except Exception as e:
                print(e)
        return super(BrandView, self).get(request, *args, **kwargs)
    
    
class CategoryView(BaseView):
    template_name = 'shop/category.html' # xxxx/xxx.html
    page_title = '' # title

    def get(self, request, *args, **kwargs):
        if "categoryID" in kwargs:
            try:
                category = Category.objects.get(id=kwargs['categoryID'])
                item = Item.objects.filter(category=category)
                self.page_title = category.name
                kwargs['item'] = item
                kwargs['category'] = category
            except Exception as e:
                print(e)
        return super(CategoryView, self).get(request, *args, **kwargs)
    
class ItemView(BaseView):
    template_name = 'shop/item.html' # xxxx/xxx.html
    page_title = '' # title

    def get(self, request, *args, **kwargs):
        if "itemID" in kwargs:
            try:
                item = Item.objects.get(id=kwargs['itemID'])
                kwargs['item'] = item
                self.page_title = item.name
            except Exception as e:
                return
        return super(ItemView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super(ItemView, self).post(request, *args, **kwargs)
