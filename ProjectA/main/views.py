from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.conf import settings
from shop.models import Brand
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


class CIndexView(BaseView):
    template_name = 'main/index.html'
    page_title = '首頁'
    
    def get(self,request):
        
        return super(CIndexView, self).get(request)
    
    