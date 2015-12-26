from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from main.views import BaseView
from account.forms import UserProfileForm, UserForm, CaptchaForm

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())
    
class UserView(LoginRequiredMixin,BaseView):
    def __init__(self, *args, **kwargs):
        super(UserView, self).__init__(*args, **kwargs)
    
    

class CSignUp(BaseView):
    template_name = 'account/signup.html'
    page_title = '註冊'
    
    def get(self, request, *args, **kwargs):
        kwargs['userForm'] = UserForm()
        kwargs['profileform'] = UserProfileForm()
        kwargs['CForm'] = CaptchaForm()
        
        return super(CSignUp, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        userForm = UserForm(request.POST)
        profileform = UserProfileForm(request.POST)
        CForm = CaptchaForm(request.POST)
        if not (CForm.is_valid() and userForm.is_valid() and profileform.is_valid()):
            kwargs['userForm'] = userForm
            kwargs['profileform'] = profileform
            kwargs['CForm'] = CForm
            return super(CSignUp, self).get(request, *args, **kwargs)
        user = userForm.save()
        user.set_password(user.password)
        user.save()
        userProfile = profileform.save(commit=False)
        userProfile.user = user
        userProfile.save()
        messages.success(request, '歡迎註冊')
        return redirect(reverse('main:main'))
    
class CSignIn(BaseView):
    template_name = 'account/signin.html'
    page_title = '登入'
    
    def get(self, request, *args, **kwargs):
        return super(CSignIn, self).get(request)
    
    def post(self,request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if not user: # authenticate fail
            kwargs['error'] = '登入失敗'
            kwargs['username'] = username
            return super(CSignIn, self).get(request, *args, **kwargs)
        if not user.is_active:
            kwargs['error'] = '帳號已停用' 
            return super(CSignIn, self).get(request, *args, **kwargs)
        login(request, user)
        messages.success(request, '登入成功')
        return redirect(reverse('main:main'))
        #return super(CSignIn, self).get(request, *args, **kwargs)

class  CSignOut(UserView):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, '歡迎再度光臨')
        return redirect(reverse('main:main'))