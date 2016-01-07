from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from datetime import datetime
from main.views import BaseView, admin_required
from main.dropbox import file_put2
from .forms import BrandForm
from shop.models import Brand
from django.db.transaction import commit

class AdminRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return admin_required(super(AdminRequiredMixin, cls).as_view())
    
class AdminView(AdminRequiredMixin,BaseView):
    def __init__(self, *args, **kwargs):
        super(AdminView, self).__init__(*args, **kwargs)
        
    def get(self, request, *args, **kwargs):
        kwargs['path'] = request.path.split("/")[1:]
        return super(AdminView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AdminView, self).get(request, *args, **kwargs)

class CAdminIndex(AdminView):
    template_name = 'control/index.html'
    page_title = '管理者'
    
    def get(self, request, *args, **kwargs):
        return super(CAdminIndex, self).get(request, *args, **kwargs)
    
class CAdminSignIn(AdminView):
    def get(self, request, *args, **kwargs):
        return redirect('/control/admin/')
    
class CBrand(AdminView):
    template_name = 'control/brand.html'
    page_title = '品牌'
    def get(self, request, *args, **kwargs):
        brand = Brand.objects.all()
        kwargs['brand'] =brand
        kwargs['number'] = list(range(len(brand)))
        return super(CBrand, self).get( request, *args, **kwargs)
    
class CBrandPreview(AdminView):
    template_name = 'control/brandpreview.html'
    page_title = '品牌'
    def get(self, request, *args, **kwargs):
        print(kwargs['brandID'])
        brand = Brand.objects.get(id=kwargs['brandID'])
        kwargs['content'] = brand.content
        return super(CBrandPreview, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        brand = Brand.objects.all()
        kwargs['brand'] =brand
        kwargs['number'] = list(range(len(brand)))
        return super(CBrandPreview, self).post(request, *args, **kwargs)
    
class CBrandAdd(AdminView):
    template_name = 'control/brandadd.html'
    page_title = '品牌管理'
    def get(self, request, *args, **kwargs):
        kwargs['form'] = BrandForm
        return super(CBrandAdd, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = BrandForm(request.POST)
        if not form.is_valid():
            kwargs['fail'] = "fail"
            return super(CBrandAdd, self).post(self, request, *args, **kwargs)
        brand = form.save(commit=False)
        if 'image' in request.FILES:
            saveName = str(datetime.strftime(datetime.now(), '%Y%m%d'))
            file = file_put2(request.FILES['image'], brand.id, saveName)
            brand.image = file
        brand.save()
            
        return redirect(reverse('control:brand'))
    
class CBrandEdit(AdminView):
    template_name = 'control/brandedit.html'
    page_title = '品牌管理'
    def get(self, request, *args, **kwargs):
        if "brandID" in kwargs:
            try:
                brand = Brand.objects.get(id=int(kwargs['brandID']))
                form = BrandForm(initial={'name':brand.name, 'description':brand.description, 'content':brand.content})
                kwargs['form'] = form
            except:
                return redirect(reverse('control:brandAdd'))
        else:
            return redirect(reverse('control:brandAdd'))
        return super(CBrandEdit, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = BrandForm(request.POST)
        if not form.is_valid():
            kwargs['fail'] = "fail"
            return super(CBrandEdit, self).post(self, request, *args, **kwargs)
        brand = form.save(commit=False)
        if 'image' in request.FILES:
            saveName = str(datetime.strftime(datetime.now(), '%Y%m%d'))
            file = file_put2(request.FILES['image'], brand.id, saveName)
            brand.image = file
        brand.save()
            
        return redirect(reverse('control:brand'))
    
class CCategory:
    template_name = 'control/category.html'
    page_title = '分類'
    
    def get(self, request, *args, **kwargs):
        return super(CCategory, self).get(request, *args, **kwargs)
    
    
    