from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.http import JsonResponse
from main.views import BaseView, get_client_ip
from account.forms import UserProfileForm, SignupForm, CaptchaForm, UserForm
from account.models import UserProfile, MyCart
from shop.models import Item

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())
    
class UserView(LoginRequiredMixin,BaseView):
    def __init__(self, *args, **kwargs):
        super(UserView, self).__init__(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super(UserView, self).get(request, *args, **kwargs)

class CSignUp(BaseView):
    template_name = 'account/signup.html'
    page_title = '註冊'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            #messages.add_message(request, 50, request.user.username+'會員登入成功', extra_tags='登入成功')
            #messages.success(request, request.user.username+'會員登入成功', extra_tags='登入成功')
            return redirect(reverse('main:main'))
        kwargs['userForm'] = SignupForm()
        kwargs['profileform'] = UserProfileForm()
        kwargs['CForm'] = CaptchaForm()
        
        return super(CSignUp, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        userForm = SignupForm(request.POST)
        profileform = UserProfileForm(request.POST)
        CForm = CaptchaForm(request.POST)
        if not (CForm.is_valid() and userForm.is_valid() and profileform.is_valid()):
            kwargs['userForm'] = userForm
            kwargs['profileform'] = profileform
            kwargs['CForm'] = CForm
            return super(CSignUp, self).get(request, *args, **kwargs)
        
        user = userForm.save()
        password = user.password
        user.set_password(password)
        user.save()
        userProfile = profileform.save(commit=False)
        userProfile.user = user
        userProfile.username = user.username
        userProfile.ip = get_client_ip(request)
        userProfile.save()
        log = authenticate(username=user.username, password=password)
        login(request, log)
        messages.add_message(request, 50, request.user.username+'會員 謝謝您的註冊', extra_tags='註冊成功')
        #messages.success(request, '歡迎註冊')
        return redirect(reverse('main:main'))
    
class CSignIn(BaseView):
    template_name = 'account/signin.html'
    page_title = '登入'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            messages.add_message(request, 50, request.user.username+'會員登入成功', extra_tags='登入成功')
            messages.success(request, request.user.username+'會員登入成功', extra_tags='登入成功')
            return redirect(reverse('main:main'))
        return super(CSignIn, self).get(request)
    
    def post(self,request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        nextPage = request.POST.get('next')
        if not user: # authenticate fail
            kwargs['error'] = '登入失敗'
            kwargs['username'] = username
            kwargs['nextPage'] = nextPage
            return super(CSignIn, self).get(request, *args, **kwargs)
        if not user.is_active:
            kwargs['error'] = '帳號已停用' 
            return super(CSignIn, self).get(request, *args, **kwargs)
        log = UserProfile.objects.get(username=username)
        log.ip = get_client_ip(request)
        log.save()
        login(request, user)
        messages.add_message(request, 50, request.user.username+'會員登入成功', extra_tags='登入成功')
        #messages.success(request, username+'會員登入成功', extra_tags='登入成功')
        return redirect(nextPage if nextPage else reverse('main:main'))

class  CSignOut(UserView):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, 50, '歡迎再度光臨', extra_tags='登出成功')
        #messages.success(request, '歡迎再度光臨', extra_tags='登出成功')
        return redirect(reverse('main:main'))
    
class CenterView(UserView):
    template_name = 'account/accountcenter.html'
    page_title = '個人資料'
    
    def get(self, request, *args, **kwargs):
        return super(CenterView, self).get(request, *args, **kwargs)
    
class CProfile(UserView):
    template_name = 'account/profile.html'
    page_title = '個人資料'
    
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        userform = UserForm(instance=user)
        profileform = UserProfileForm(instance=user.userprofile)
         
        kwargs['userform'] = userform
        kwargs['profileform'] = profileform
        return super(CProfile, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        userform = UserForm(request.POST, instance=user)
        profileform = UserProfileForm(request.POST, instance=user.userprofile)

        if not (userform.is_valid() and profileform.is_valid()):
            kwargs['userform'] = userform
            kwargs['profileform'] = profileform
            return super(CProfile, self).post(request, *args, **kwargs)
        
        profileform.save()
        user = userform.save()
        password = userform.cleaned_data.get('password')
        if password:
            user.set_password(password)
            user.save()
            log = authenticate(username=user.username, password=password)
            login(request, log)
        messages.success(request, '會員資料修改成功')
        
        return redirect(reverse('account:profile'))
    
class MyCartView(UserView):
    template_name = 'account/mycart.html' # xxxx/xxx.html
    page_title = '購物車' # title

    def get(self, request, *args, **kwargs):
        
        return super(MyCartView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        qty = int(request.POST.get('qty'))
        itemID= request.POST.get('itemID')
        item = Item.objects.get(id=itemID)
        success = False
        try:
            mycart = MyCart.objects.get(itemID=item)
            mycart.Qty+=qty
            mycart.save()
            success = True
        except Exception as e:
            MyCart.objects.create(itemID=item,Qty=qty, user=request.user)
            success = True
            print(e)
        response = {}
        response["success"] = success
        response["qty"] = qty
        response["itemName"] = item.name
        return JsonResponse(response)
    
    def getPostData(self):
        return