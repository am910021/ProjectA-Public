from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required 
from django.conf import settings
from .models import Notice
from shop.models import Brand, Item
from account.models import MyCart

def admin_required(fun):
    def auth(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect(settings.LOGIN_URL +'?next=%s' % request.path)
        if not request.user.is_superuser==True:
            return redirect(reverse('main:main'))
        return fun(request, *args, **kwargs)
    return auth

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class BaseView(TemplateView):

    # Base template to extend in drived views
    base_template_name = 'main/base.html'

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
            
        # Settings context data for base template
        context['SITE_NAME'] = settings.SITE_NAME
        context['base_template_name'] = self.base_template_name
        context['brandMenu'] = Brand.objects.all()
        if hasattr(self, 'page_title'):
            context['page_title'] = self.page_title

        return context
    
    def get(self, request, *args, **kwargs):
        if request.user.username!="":
            kwargs['mycartNum']=len(MyCart.objects.filter(user=request.user))
        return super(BaseView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        if request.user.username!="":
            kwargs['mycartNum']=len(MyCart.objects.filter(user=request.user))
        return super(BaseView, self).get(request, *args, **kwargs)

    def getHost(self, request):
        return request.META['HTTP_HOST']
    
    def getPost(self, request):
        return request.META['SERVER_PORT']
    
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())
    
class UserBase(LoginRequiredMixin,BaseView):
    def __init__(self, *args, **kwargs):
        super(UserBase, self).__init__(*args, **kwargs)


class IndexView(BaseView):
    template_name = 'main/index2.html'
    page_title = '首頁'
    
    def get(self, request, *args, **kwargs):
        try:
            notice = Notice.objects.all().order_by("-date")
            kwargs['notice'] = notice[:10]
        except Exception as e:
            print(e)
            
        try:
            deals = Item.objects.filter(sp=True, isActive=True)
            kwargs['deals'] = deals[:3]
        except Exception as e:
            print(e)
        
        try:
            new = Item.objects.filter(new=True, isActive=True)
            kwargs['first'] = new[0]
            kwargs['new'] = new[1:5]
            kwargs['number'] = list(range(len(new[1:5])))
        except Exception as e:
            print(e)
        return super(IndexView, self).get(request, *args, **kwargs)
    
class NoticeView(BaseView):
    template_name = 'main/notice/notice.html' # xxxx/xxx.html
    page_title = '公告' # title

    def get(self, request, *args, **kwargs):
        post = Notice.objects.all().order_by("-date")
        kwargs['post'] = post
        kwargs['number'] = list(range(len(post)))
        return super(NoticeView, self).get(request, *args, **kwargs)

class NoticeDetial(BaseView):
    template_name = 'main/notice/detail.html' # xxxx/xxx.html
    page_title = '公告' # title

    def get(self, request, *args, **kwargs):
        if 'noticeID' not in kwargs:
            return redirect(reversed('main:notice'))
        try:
            notice = Notice.objects.get(id=kwargs['noticeID'])
            kwargs['notice'] = notice
        except Exception as e:
            print(e)
            return redirect(reversed('main:notice'))
        return super(NoticeDetial, self).get(request, *args, **kwargs)

class Deals(BaseView):
    template_name = 'main/deals.html' # xxxx/xxx.html
    page_title = '特賣商品' # title

    def get(self, request, *args, **kwargs):
        item = Item.objects.filter(sp=True, isActive=True)
        kwargs['item'] = item
        return super(Deals, self).get(request, *args, **kwargs)

    