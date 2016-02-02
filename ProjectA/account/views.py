# -*- coding: utf-8 -*-
import datetime, time
import random
from django.utils import timezone
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from main.views import BaseView, UserBase, get_client_ip
from main.sendEmail import SMTP
from account.forms import ProfileForm, SignupForm, CaptchaForm, UserForm, CheckOutForm, ResetPwd
from account.models import Profile, MyCart, Order, GroupOrder
from shop.models import Item
from pyaes.aescipher import AESCipher
from pay2go.views import BuyData

def timeFormat(time):
    return str(datetime.datetime.strftime(time, '%Y%m%d'))


class CSignUp(BaseView):
    template_name = 'account/signup.html'
    page_title = '註冊'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            #messages.add_message(request, 50, request.user.username+'會員登入成功', extra_tags='登入成功')
            #messages.success(request, request.user.username+'會員登入成功', extra_tags='登入成功')
            return redirect(reverse('main:main'))
        kwargs['userForm'] = SignupForm()
        kwargs['profileform'] = ProfileForm()
        kwargs['CForm'] = CaptchaForm()
        
        return super(CSignUp, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        userForm = SignupForm(request.POST)
        profileform = ProfileForm(request.POST)
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
        log = Profile.objects.get(username=username)
        log.ip = get_client_ip(request)
        log.save()
        login(request, user)
        messages.add_message(request, 50, request.user.username+'會員登入成功', extra_tags='登入成功')
        #messages.success(request, username+'會員登入成功', extra_tags='登入成功')
        return redirect(nextPage if nextPage else reverse('main:main'))

class  CSignOut(UserBase):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, 50, '歡迎再度光臨', extra_tags='登出成功')
        #messages.success(request, '歡迎再度光臨', extra_tags='登出成功')
        return redirect(reverse('main:main'))
    
class ForgetView(BaseView):
    template_name = 'account/forget.html' # xxxx/xxx.html
    page_title = '忘記密嗎'

    def get(self, request, *args, **kwargs):
        return super(ForgetView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        response = {'dataError':True, 'success':False}
        if not ("username" in request.POST and "email" in request.POST):
            response['formNull'] = True
            return super(ForgetView, self).post(request, *args, **kwargs)
        try:
            kwargs['username'] = request.POST.get("username")
            kwargs['email'] = request.POST.get("email")
            user = User.objects.get(username=request.POST.get("username"))
            if user.email==request.POST.get("email"):
                resetCode = self.createCode(12)
                user.profile.resetCode=resetCode
                user.profile.save()
                response['dataError']=False
                response['success']= self.sendMail(request, user,resetCode)
        except Exception as e:
            print(e)
    
        return JsonResponse(response)
    
    def sendMail(self,request, user, resetCode):
        
        timeout = datetime.datetime.strftime(timezone.now()+ datetime.timedelta(hours=24), '%Y-%m-%d-%H-%M-%S')
        cipher = AESCipher()
        code = cipher.encrypt(str(user.id)+"~|@|~"+user.username+"~|@|~"+user.email+"~|@|~"+resetCode+
                              "~|@|~"+timeout )
        
        url = "http://"+self.getHost(request)+reverse('account:forgetReset', args=(code,))
        email = user.email
        html="""
            <!DOCTYPE html>
            <html>
            <body>
            <span>這是您的重置碼（分大小寫）：</span><span style="background-color:#eee">{code}</span><br>
            以下是重置您密碼的網址：<br>
            <a href="{url}" target="_blank">點此重置您密碼</a>
            </body>
            </html>
        """.format(url=url, name=user.username, code = resetCode)
        text = "這是您的重置碼(分大小寫)：\n {code} \n 以下是重置您密碼的網址：\n{url}".format(url=url, code = resetCode)
        smtp = SMTP()
        
        return smtp.send(email, "密碼重置", html , text) # 收件人, 標題, 內容
    
    def createCode(self, num):
        n,l,u=0,0,0
        s=""
        i=0
        m = num//3
        while(True):
            r=random.randint(1,3)
            if r==1 and (n<m or i>0):
                n+=1
                s+=chr(random.randint(48,57))
            if r==2 and (l<m or i>0):
                l+=1
                s+=chr(random.randint(97,122))
            if r==3 and (u<m or i>0):
                u+=1
                s+=chr(random.randint(65,90))
            if n+l+u>=m*3:
                i+=1
            if n+l+u>=num:
                break
        return s
    
class ForgetReset(BaseView):
    template_name = 'account/reset.html' # xxxx/xxx.html
    page_title = '重置密碼' # title

    def get(self, request, *args, **kwargs):
        if not "base64string" in kwargs:
            kwargs['getError'] = True
            return super(ForgetReset, self).get(request, *args, **kwargs)
        
        aes = AESCipher()
        data=None
        try:
            data = aes.decrypt(kwargs['base64string']).split("~|@|~")
        except Exception as e:
            print(e)
            kwargs['getError'] = True
            return super(ForgetReset, self).get(request, *args, **kwargs)
        
        timeout = time.mktime(time.strptime(data[4], '%Y-%m-%d-%H-%M-%S'))
        now = time.mktime(timezone.now().timetuple())
        
        if  now>timeout:
            kwargs['timeout'] = "重置資料已超時，請重新按 忘記密碼。"
            return super(ForgetReset, self).get(request, *args, **kwargs)
        
        try:
            user = User.objects.get(id=data[0])
            if (user.username!=data[1] and user.email!=data[2] and user.profile.resetCode!=data[3]):
                kwargs['getError'] = True
            kwargs['form'] = ResetPwd()
        except Exception as e:
            print(e)

        
        return super(ForgetReset, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = ResetPwd(request.POST)
        kwargs['form']=form
        if not form.is_valid():
            return super(ForgetReset, self).post(request, *args, **kwargs)
        username = request.POST.get('username')
        password = request.POST.get('password')
        code = request.POST.get('code')
        try:
            user = User.objects.get(username=username)
            if user.profile.resetCode!=code:
                kwargs['postError'] = True
                return super(ForgetReset, self).post(request, *args, **kwargs)
            user.profile.resetCode=""
            user.profile.save()
            user.set_password(password)
            user.save()
            kwargs['success'] = True
        except Exception as e:
            print(e)
            kwargs['postError'] = True
        return super(ForgetReset, self).post(request, *args, **kwargs)
        
    
class CenterView(UserBase):
    template_name = 'account/center.html'
    page_title = '個人資料'
    
    def get(self, request, *args, **kwargs):
        return super(CenterView, self).get(request, *args, **kwargs)
    
class CProfile(UserBase):
    template_name = 'account/profile.html'
    page_title = '個人資料'
    
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        userform = UserForm(instance=user)
        profileform = ProfileForm(instance=user.profile)
         
        kwargs['userform'] = userform
        kwargs['profileform'] = profileform
        return super(CProfile, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        userform = UserForm(request.POST, instance=user)
        profileform = ProfileForm(request.POST, instance=user.profile)

        if request.POST.get('email')!=user.email:
            user.profile.isVerified=False
            user.profile.save()

        if not (userform.is_valid() and profileform.is_valid()):
            kwargs['userform'] = userform
            kwargs['profileform'] = profileform
            return super(CProfile, self).post(request, *args, **kwargs)
        if userform.cleaned_data.get('email')!=user.email:
            user.profile.isVerified=False
            user.profile.save()
        
        profileform.save()
        userform.save()
        password = userform.cleaned_data.get('password')
        if password:
            user.set_password(password)
            user.save()
            log = authenticate(username=user.username, password=password)
            login(request, log)
        messages.success(request, '會員資料修改成功')
        
        return redirect(reverse('account:profile'))

class Verification(UserBase):
    template_name = 'account/verification.html' # xxxx/xxx.html
    page_title = '驗證區' # title

    def get(self, request, *args, **kwargs):
        kwargs['get'] = True
        kwargs['mail'] = SMTP()
        return super(Verification, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        cipher = AESCipher()
        code = cipher.encrypt(str(request.user.id)+"~|@|~"+request.user.username+"~|@|~"+request.user.email)
        url = "http://"+self.getHost(request)+reverse('account:verifyEmail', args=(code,))
        email = request.user.email
        html="""
            <!DOCTYPE html>
            <html>
            <body>
            <h3>會員 {name}:</h3>
            <p>謝謝您的註冊。</p>
            
            以下是您的驗證網址：
            <a href="{url}">點此驗證</a>
            </body>
            </html>
        """.format(url=url, name=request.user.username)
        text = "以下是你的驗證網址：\n {url}".format(url=url)
        response = {}
        smtp = SMTP()
        response['success'] = smtp.send(email, "Email 驗證", html , text) # 收件人, 標題, 內容
        return JsonResponse(response)


class VerificationEemail(BaseView):
    template_name = "account/verification.html"
    page_title = '電子郵件驗證'
    
    def get(self,request, *args, **kwargs):
        if not "base64string" in kwargs:
            kwargs['passed'] = False
            return super(VerificationEemail, self).get(request, *args, **kwargs)
        kwargs['passed'] = self.checkUser(request, *args, **kwargs)
        return super(VerificationEemail, self).get(request, *args, **kwargs)
        
    def checkUser(self,request, *args, **kwargs):
        base64 = kwargs['base64string']
        aes = AESCipher()
        data = aes.decrypt(base64).split("~|@|~")
        user = User.objects.get(id=data[0])
        if user.username!=data[1]:
            return False
        if user.email!=data[2]:
            return False
        user.profile.isVerified = True
        user.profile.save()
        logout(request)
        return True


class MyCartView(UserBase):
    template_name = 'account/mycart.html' # xxxx/xxx.html
    page_title = '購物車' # title

    def get(self, request, *args, **kwargs):
        mycart = MyCart.objects.filter(user=request.user)
        kwargs['mycart'] =mycart
        kwargs['number'] = list(range(len(mycart)))
        return super(MyCartView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        qty = int(request.POST.get('qty'))
        itemID= request.POST.get('itemID')
        item = Item.objects.get(id=itemID)
        success = False
        try:
            mycart = MyCart.objects.get(itemID=item)
            mycart.qty+=qty
            mycart.save()
            success = True
        except Exception as e:
            MyCart.objects.create(itemID=item, qty=qty, user=request.user)
            success = True
            print(e)
        response = {}
        response["success"] = success
        response["qty"] = len(MyCart.objects.all())
        response["itemName"] = item.name
        return JsonResponse(response)
    
def removeItem(request):
    if request.method=='GET':
        return redirect(reverse('account:mycart'))
    
    removeID= request.POST.get('removeID')
    try:
        item = MyCart.objects.get(id=removeID)
        messages.success(request, '商品： '+ item.itemID.name +' 移除成功。')
        item.delete()
    except Exception as e:
        messages.error(request, '移除失敗。')
        print(e)
    return redirect(reverse('account:mycart'))
    
class Agreement(UserBase):
    template_name = 'account/checkout/agreement.html'
    page_title = "結帳-合約"

    def get(self, request, *args, **kwargs):
        return super(Agreement, self).get(request, *args, **kwargs)
    
class CheckOut(UserBase):
    template_name = 'account/checkout/info.html' # xxxx/xxx.html
    page_title = '結帳-資訊' # title

    def get(self, request, *args, **kwargs):
        return redirect(reverse('account:mycart'))
    
    def post(self, request, *args, **kwargs):
        if "byAgreement" in request.POST:
            kwargs['form'] = CheckOutForm()
            return super(CheckOut, self).get(request, *args, **kwargs)
        if "reSet" in request.POST:
            kwargs['form'] = CheckOutForm()
            return super(CheckOut, self).get(request, *args, **kwargs)
        if "changeForm" in request.POST:
            kwargs['form'] = CheckOutForm(request.POST)
            return super(CheckOut, self).get(request, *args, **kwargs)
        if "byInfo" in request.POST:
            return self.checkInfo(request, *args, **kwargs)
        if "byData" in request.POST:
            return self.checkdata(request, *args, **kwargs)
        
        return super(CheckOut, self).post(request, *args, **kwargs)
    
    
    def checkInfo(self, request, *args, **kwargs):
        kwargs['form'] = CheckOutForm(request.POST)
        if not kwargs['form'].is_valid():
            return super(CheckOut, self).post(request, *args, **kwargs)
        self.template_name = 'account/checkout/data.html' # xxxx/xxx.html
        self.page_title = '結帳-確認' # title
        kwargs['form'].setReadOnly()
        mycart = MyCart.objects.filter(user=request.user)
        kwargs['mycart'] =mycart
        kwargs['number'] = list(range(len(mycart)))
        kwargs["timeout"] = datetime.datetime.strftime(timezone.now()+ datetime.timedelta(hours=1), '%Y-%m-%d-%H-%M-%S')
        return super(CheckOut, self).post(request, *args, **kwargs)
    
    def checkdata(self, request, *args, **kwargs):
        timeout =  time.mktime(time.strptime(request.POST.get('timeout'), '%Y-%m-%d-%H-%M-%S'))
        now = time.mktime(timezone.now().timetuple())
        if now > timeout:
            messages.error(request, '本次結帳時間超時，請重新整理頁面。')
            return redirect(reverse('account:agreement'))

        form = request.POST
        group = GroupOrder.objects.create(user=request.user)
        group.payerName = form.get('payerName')
        group.payerAddress = form.get('payerAddress')
        group.payerPhone = form.get('payerPhone')
        group.recipientName = form.get('recipientName')
        group.recipientAddress = form.get('recipientAddress')
        group.recipientPhone = form.get('recipientPhone')
        totalamount = 0
        mycart  = MyCart.objects.all()
        for i in mycart:
            subtotal = i.itemID.cost * i.qty
            Order.objects.create(group=group, itemID=i.itemID, itemNmae=i.itemID.name,itemPrice=subtotal, qty=i.qty)
            totalamount+=subtotal
            i.itemID.inventory = i.itemID.inventory-i.qty
            i.itemID.save()
            #i.delete()
        
        group.totalAmount=totalamount
        group.save()
        return redirect(reverse('account:order', args=("checkout", group.id)))

    
    
class OrderView(UserBase):
    template_name = 'account/order.html' # xxxx/xxx.html
    page_title = "結帳-錯誤"
    
    def get(self, request, *args, **kwargs):
        if not ("groupID" in kwargs and "method" in kwargs):
            return super(OrderView, self).get(request, *args, **kwargs)
            
        try:
            group = GroupOrder.objects.filter(user=request.user).get(id=kwargs['groupID'])
        except Exception as e:
            print(e)
            return super(OrderView, self).get(request, *args, **kwargs)

        order = Order.objects.filter(group=group)
        kwargs['group'] = group
        kwargs['order'] = order
        kwargs['number'] = list(range(len(order)))
        MerchantOrderNo = timeFormat(group.date)+str(group.id)
        Amt = str(group.totalAmount)
        Email = request.user.email
        ItemDesc = "123"
        data = BuyData(MerchantOrderNo, Amt, Email, ItemDesc, self.getHost(request))
        kwargs['BuyData'] = data
        kwargs['success'] = True
        
        if kwargs['method']=="checkout":
            self.page_title = '結帳-完成'
        else:
            self.page_title = '訂單'+MerchantOrderNo
            
        return super(OrderView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return redirect(reverse('account:center'))
    
    