import random
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
import datetime
from main.models import Setting, Notice
from main.views import BaseView, admin_required
from main.dropbox import file_put2, file_delete
from .forms import BrandForm, CategoryForm, ItemForm, PostForm
from shop.models import Brand, Category, Item
from django.utils import timezone
from account.models import GroupOrder

class AdminRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return admin_required(super(AdminRequiredMixin, cls).as_view())
    
class AdminBase(AdminRequiredMixin,BaseView):
    def __init__(self, *args, **kwargs):
        super(AdminBase, self).__init__(*args, **kwargs)
        
class CAdminIndex(AdminBase):
    template_name = 'control/index.html'
    page_title = '管理者'
    
    def get(self, request, *args, **kwargs):
        return super(CAdminIndex, self).get(request, *args, **kwargs)
    
def redirectAdminIndex(request):
    return redirect(reverse('control:admin'))
    
    
class CAdminSignIn(AdminBase):
    def get(self, request, *args, **kwargs):
        return redirect('/control/admin/')
    
class CBrand(AdminBase):
    template_name = 'control/brand/brand.html'
    page_title = '品牌'
    
    def get(self, request, *args, **kwargs):
        brand = Brand.objects.all().order_by('id')
        kwargs['brand'] =brand
        kwargs['number'] = list(range(len(brand)))
        return super(CBrand, self).get( request, *args, **kwargs)
    
class CBrandPreview(AdminBase):
    template_name = 'control/brand/preview.html'
    page_title = '品牌'
    
    def get(self, request, *args, **kwargs):
        brand = Brand.objects.get(id=kwargs['brandID'])
        kwargs['content'] = brand.content
        return super(CBrandPreview, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        brandform = BrandForm(request.POST)
        brandform.is_valid()
        kwargs['content'] = brandform.cleaned_data.get('content')
        return super(CBrandPreview, self).post(request, *args, **kwargs)
    
class CBrandAdd(AdminBase):
    template_name = 'control/brand/add.html'
    page_title = '品牌管理'
    
    def get(self, request, *args, **kwargs):
        kwargs['form'] = BrandForm()
        return super(CBrandAdd, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = BrandForm(request.POST)
        if not form.is_valid():
            kwargs['form'] = form
            return super(CBrandAdd, self).post(self, request, *args, **kwargs)
        brand = form.save()
        if 'image' in request.FILES:
            brand.image = file_put2(request.FILES['image'], brand.id, 'brand')
            brand.save()
        return redirect(reverse('control:brand'))
    
class CBrandEdit(AdminBase):
    template_name = 'control/brand/edit.html'
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
            if brand.image!="":
                file_delete(brand.image.split("/")[1])
            
            
            brand.image = file_put2(request.FILES['image'], brand.id, 'brand')
            brand.save()
        return redirect(reverse('control:brand'))
    
class CCategory(AdminBase):
    template_name = 'control/category/category.html'
    page_title = '分類'
    
    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        kwargs['category'] = category
        kwargs['number'] = list(range(len(category)))
        return super(CCategory, self).get(request, *args, **kwargs)
    
class CCategoryAdd(AdminBase):
    template_name = 'control/category/add.html'
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
            category.image = file_put2(request.FILES['image'], category.id, 'category')
            category.save()
        return redirect(reverse('control:category'))
    
class CCategoryEdit(AdminBase):
    template_name = 'control/category/edit.html'
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
            if category.image!="":
                file_delete(category.image.split("/")[1])
                
            category.image = file_put2(request.FILES['image'], category.id, 'category')
            category.save()
        return redirect(reverse('control:category'))
    
class ItemManage(AdminBase):
    template_name = 'control/item/item.html' # xxxx/xxx.html
    page_title = '商品管理' # title

    def get(self, request, *args, **kwargs):
        item = Item.objects.all()
        kwargs['item'] = item
        kwargs['number'] = list(range(len(item)))
        return super(ItemManage, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super(ItemManage, self).post(request, *args, **kwargs)
    
class ItemAdd(AdminBase):
    template_name = 'control/item/add.html' # xxxx/xxx.html
    page_title = '新增商品' # title

    def get(self, request, *args, **kwargs):
        kwargs['form'] = ItemForm()
        return super(ItemAdd, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = ItemForm(request.POST)
        
        if not form.is_valid():
            kwargs['form'] = form
            return super(ItemAdd, self).post(request, *args, **kwargs)
        item = form.save()
        if 'image' in request.FILES:
            item.image = file_put2(request.FILES['image'], item.id, 'item')
        if 'image2' in request.FILES:
            item.image2 = file_put2(request.FILES['image2'], item.id, 'item2')
        item.save()
            
        
        
        messages.success(request, '商品：'+request.POST.get('name')+"上架成功")
        
        return redirect(reverse('control:item'))
        #return super(ItemAdd, self).post(request, *args, **kwargs)
    
class ItemEdit(AdminBase):
    template_name = 'control/item/edit.html' # xxxx/xxx.html
    page_title = '編輯商品' # title

    def get(self, request, *args, **kwargs):
        if "itemID" in kwargs:
            try:
                item = Item.objects.get(id=kwargs['itemID'])
                form = ItemForm(instance=item)
                kwargs['form'] = form
            except Exception as e:
                print(e)
                return redirect(reverse('control:itemAdd'))
        return super(ItemEdit, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        item = Item.objects.get(id=kwargs['itemID'])
        form = ItemForm(request.POST, instance=item)
        if not form.is_valid():
            kwargs['form'] = form
            return super(ItemEdit, self).post(request, *args, **kwargs)
        item = form.save()
        if 'image' in request.FILES:
            if item.image!="":
                file_delete(item.image.split("/")[1],"item")
            item.image = file_put2(request.FILES['image'], item.id, 'item')
        if 'image2' in request.FILES:
            if item.image2!="":
                file_delete(item.image2.split("/")[1],"item2")
            item.image2 = file_put2(request.FILES['image2'], item.id, 'item2')
        item.save()
        messages.success(request, '商品：'+request.POST.get('name')+"已更新成功")        
        return redirect(reverse('control:item'))
    
class ItemPreview(AdminBase):
    template_name = 'control/item/preview.html' # xxxx/xxx.html
    page_title = '商品預覽' # title

    def get(self, request, *args, **kwargs):
        if "itemID" in kwargs:
            try:
                item = Item.objects.get(id=kwargs['itemID'])
                kwargs['item'] = item
            except Exception as e:
                return
        return super(ItemPreview, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super(ItemPreview, self).post(request, *args, **kwargs)
    
    
class VConfig(AdminBase):
    template_name = 'control/config/config.html' # xxxx/xxx.html
    page_title = '基本設定' # title

    def get(self, request, *args, **kwargs):
        category = Setting.objects.get_or_create(name="category")[0]
        kwargs['isActive'] = category.isActive
        kwargs['time'] = category.time
        return super(VConfig, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        category = Setting.objects.get_or_create(name="category")[0]
        category.isActive = True if request.POST.get('isActive') else False
        category.save()
        
        messages.success(request, '設定成功')
        return redirect(reverse('control:config'))
    
class ConfigEmail(AdminBase):
    template_name = 'control/config/email.html' # xxxx/xxx.html
    page_title = 'Email 寄信設定' # title

    def get(self, request, *args, **kwargs):
        gmail = Setting.objects.get_or_create(name="gmailAccount")[0]
        kwargs['data'] = [gmail.c1, gmail.c2, gmail.isActive, gmail.time]
        return super(ConfigEmail, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        gmail = Setting.objects.get_or_create(name="gmailAccount")[0]
        gmail.c1 = request.POST.get('account')
        gmail.c2 = request.POST.get('password')
        gmail.isActive = True if request.POST.get('isActive') else False
        gmail.save()
        messages.success(request, '設定成功')
        return redirect(reverse('control:configEmail'))

class ConfigPay2Go(AdminBase):
    template_name = 'control/config/pay2go.html' # xxxx/xxx.html
    page_title = 'Pay2GO 設定' # title

    def get(self, request, *args, **kwargs):
        pay2go = Setting.objects.get(name="pay2go")
        kwargs['data'] = [pay2go.c1, pay2go.c2, pay2go.c3, pay2go.c4, pay2go.isActive, pay2go.time ]
        return super(ConfigPay2Go, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = request.POST
        pay2go = Setting.objects.get(name="pay2go")
        pay2go.c1= form.get('memberID')
        pay2go.c2= form.get('hashKEY')
        pay2go.c3= form.get('hashIV')
        pay2go.c4= True if form.get('isTest') else False
        pay2go.isActive= True if form.get('isActive') else False
        pay2go.save()
        messages.success(request, '設定成功')
        return redirect(reverse('control:configPay2go'))
    
class ConfigKey(AdminBase):
    template_name = 'control/config/key.html' # xxxx/xxx.html
    page_title = '系統金鑰設定' # title

    def get(self, request, *args, **kwargs):
        key = Setting.objects.get(name="key")
        kwargs['data'] = (key.c1, key.time)
        return super(ConfigKey, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = request.POST
        key = Setting.objects.get(name="key")
        key.c1=form.get('key') if form.get('key')!="" else self.createCode(30)
        key.save()
        messages.success(request, '設定成功')
        return redirect(reverse('control:configKey'))
    
class OrderView(AdminBase):
    template_name = 'control/order/list.html' # xxxx/xxx.html
    s=("未處理","處理中","配送中","已完成")

    def get(self, request, *args, **kwargs):
        if 'status' not in kwargs or int(kwargs['status'])>4:
            group = GroupOrder.objects.filter(status__range=(0,2))
            kwargs['status']='0'
            self.page_title = "未完成訂單"
        else:
            status = int(kwargs['status'])
            group = GroupOrder.objects.filter(status=status)
            self.page_title = self.s[status]+"訂單"
            
        kwargs['groups']=group
        kwargs['number'] = list(range(len(group)))
        return super(OrderView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        try:
            groupID = int(request.POST.get('groupID'))
            status = int(request.POST.get('setStatus'))
            group = GroupOrder.objects.get(id=groupID)
            group.status=status
            group.save()
            msg = self.s[status]
            messages.add_message(request, 50, group.number, extra_tags=msg)    
        except Exception as e:
            print(e)
        return redirect(reverse('control:order', args=(status-1,)))
    
class NoticeView(AdminBase):
    template_name = 'control/notice/notice.html' # xxxx/xxx.html
    page_title = '公告管理' # title

    def get(self, request, *args, **kwargs):
        post = Notice.objects.all().order_by("-date")
        kwargs['post'] = post
        kwargs['number'] = list(range(len(post)))
        return super(NoticeView, self).get(request, *args, **kwargs)
    
class NoticePost(AdminBase):
    template_name = 'control/notice/post.html' # xxxx/xxx.html
    page_title = '發布公告' # title

    def get(self, request, *args, **kwargs):
        kwargs['form'] = PostForm()
        return super(NoticePost, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if not form.is_valid():
            kwargs['form'] = form
            return super(NoticePost, self).post(request, *args, **kwargs)
        
        form.save()
        messages.success(request, request.POST.get('title'))
        return redirect(reverse('control:notice'))