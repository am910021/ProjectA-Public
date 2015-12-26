from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from main.views import BaseView, get_client_ip
from account.forms import UserProfileForm, SignupForm, CaptchaForm, ModifyForm
from account.models import UserProfile
from django.contrib.auth.models import User

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
        user.set_password(user.password)
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
        log = UserProfile.objects.get(username=username)
        log.ip = get_client_ip(request)
        log.save()
        
        nextPage = request.POST.get('next')
        if not user: # authenticate fail
            kwargs['error'] = '登入失敗'
            kwargs['username'] = username
            kwargs['nextPage'] = nextPage
            return super(CSignIn, self).get(request, *args, **kwargs)
        if not user.is_active:
            kwargs['error'] = '帳號已停用' 
            return super(CSignIn, self).get(request, *args, **kwargs)
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
    
class CMy(UserView):
    template_name = 'account/myaccount.html'
    page_title = '個人資料'
    
    def get(self, request, *args, **kwargs):
        return UserView.get(self, request, *args, **kwargs)
    
class CProfile(UserView):
    template_name = 'account/profile.html'
    page_title = '個人資料'
    
    def get(self, request, *args, **kwargs):
        modifyform = ModifyForm()
        modifyform.readonly('username')
        modifyform.value(request.user.username)
        kwargs['modifyForm'] = modifyform
        return super(CProfile, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        modifyform = ModifyForm(request.POST)
        if not modifyform.is_valid():
            kwargs['modifyForm'] = modifyform
            return super(CProfile, self).post(request, *args, **kwargs)
        
        data = modifyform.cleaned_data
        userProfile = UserProfile.objects.get(username=data.get('username'))
        userProfile.user.set_password(data.get('password'))
        userProfile.user.email = data.get('email')
        userProfile.user.save()
        userProfile.fullName = data.get('fullName')
        userProfile.address = data.get('address')
        userProfile.phone = data.get('phone')
        userProfile.save()
        
        user = authenticate(username=data.get('username'), password=data.get('password'))
        login(request, user)
        messages.success(request, "帳號修改成功")
        return redirect(reverse('account:profile'))
    