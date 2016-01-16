from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from datetime import datetime
from main.models import Setting
from main.views import BaseView, admin_required
from main.dropbox import file_put2, file_delete
from .forms import BrandForm, CategoryForm, EnableCategory
from shop.models import Brand, Category

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
        brand = Brand.objects.all().order_by('id')
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
            kwargs['form'] = form
            return super(CBrandAdd, self).post(self, request, *args, **kwargs)
        brand = form.save()
        if 'image' in request.FILES:
            brand.image = file_put2(request.FILES['image'], brand.id)
            brand.save()
        return redirect(reverse('control:brand'))
    
class CBrandEdit(AdminView):
    template_name = 'control/brandedit.html'
    page_title = '品牌管理'
    
    def get(self, request, *args, **kwargs):
        if "brandID" in kwargs:
            try:
                brand = Brand.objects.get(id=kwargs['brandID'])
                form = BrandForm(instance=brand)
                kwargs['form'] = form
            except:
                return redirect(reverse('control:brandAdd'))
        else:
            return redirect(reverse('control:brandAdd'))
        return super(CBrandEdit, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        branddb = Brand.objects.get(id=kwargs['brandID'])
        form = BrandForm(request.POST, instance=branddb)
        if not form.is_valid():
            kwargs['form'] = form
            return super(CBrandEdit, self).post(self, request, *args, **kwargs)
        brand = form.save()
        if 'image' in request.FILES:
            file_delete(brand.image.split("/")[1])
            brand.image = file_put2(request.FILES['image'], brand.id)
            brand.save()
        return redirect(reverse('control:brand'))
    
class CCategory(AdminView):
    template_name = 'control/category.html'
    page_title = '分類'
    
    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        kwargs['category'] = category
        kwargs['number'] = list(range(len(category)))
        return super(CCategory, self).get(request, *args, **kwargs)
    
class CCategoryAdd(AdminView):
    template_name = 'control/categoryadd.html'
    page_title = '分類'
    
    def get(self, request, *args, **kwargs):
        kwargs['form'] = CategoryForm()
        return super(CCategoryAdd, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if not form.is_valid():
            kwargs['form'] = form
            return super(CCategoryAdd, self).get(request, *args, **kwargs)
        category = form.save()
        if 'image' in request.FILES:
            category.image = file_put2(request.FILES['image'], category.id)
            category.save()
        return redirect(reverse('control:category'))
    
class CCategoryEdit(AdminView):
    template_name = 'control/categoryedit.html'
    page_title = '分類'
    
    def get(self, request, *args, **kwargs):
        if "categoryID" in kwargs:
            try:
                category = Category.objects.get(id=kwargs['categoryID'])
                form = CategoryForm(instance=category)
                kwargs['form'] = form
            except:
                return redirect(reverse('control:CategorydAdd'))
        else:
            return redirect(reverse('control:CategorydAdd'))
        return super(CCategoryEdit, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        categorydb = Category.objects.get(id=kwargs['categoryID'])
        form = CategoryForm(request.POST, instance=categorydb)
        if not form.is_valid():
            kwargs['form'] = form
            return super(CCategoryEdit, self).post(self, request, *args, **kwargs)
        category = form.save()
        if 'image' in request.FILES:
            file_delete(category.image.split("/")[1])
            category.image = file_put2(request.FILES['image'], category.id)
            category.save()
        return redirect(reverse('control:category'))
    
class VConfig(AdminView):
    template_name = 'control/config.html' # xxxx/xxx.html
    page_title = '基本設定' # title

    def get(self, request, *args, **kwargs):
        category = Setting.objects.filter(name="category")[0]
        kwargs['enableCategory'] = EnableCategory(instance=category)
        return super(VConfig, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super(VConfig, self).post(request, *args, **kwargs)
    