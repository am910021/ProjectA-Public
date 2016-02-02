from datetime import datetime, timedelta
import hashlib
from django.shortcuts import render, HttpResponse,redirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from main.models import Setting
from main.views import BaseView, UserBase
from account.models import GroupOrder
from .forms import BuyForm, NotifyUrlResponse, CustomerUrlResponse
from .models import CustomerUrlDB, NotifyUrlDB

class setting:
    def __init__(self):
        set = Setting.objects.get(name="pay2go")
        self.memberID = set.c1
        self.hashKEY = set.c2
        self.hashIV = set.c3
        self.isTest = True if set.c4=="True" else False
        self.isActive = set.isActive
        print(self.isActive)
        if self.memberID=="" or self.hashIV=="" or self.hashKEY=="":
            self.isActive = False
        

def timeFormat(time):
    return str(datetime.strftime(time, '%Y%m%d'))


def time():
    return datetime.now()+ timedelta(hours=8)

@csrf_exempt
def NotifyURL(request):
    if request.method=="POST":
        form = NotifyUrlResponse(request.POST)
        if form.is_valid():
            MerchantID = form.cleaned_data['MerchantID']
            Amt = form.cleaned_data['Amt']
            MerchantOrderNo = form.cleaned_data['MerchantOrderNo']
            TradeNo = form.cleaned_data['TradeNo']
            code = CheckCode(MerchantID, Amt, MerchantOrderNo, TradeNo)
            if code==form.cleaned_data['CheckCode']:
                form.save()
    return HttpResponse()

def CheckCode(MerchantID, Amt, MerchantOrderNo, TradeNo):
    db = setting()
    CheckValue = "HashIV=" + db.hashIV
    CheckValue+= "&Amt=" + str(Amt)
    CheckValue+= "&MerchantID=" + MerchantOrderNo
    CheckValue+= "&MerchantOrderNo=" + MerchantOrderNo
    CheckValue+= "&TradeNo=" + TradeNo
    CheckValue+= "&HashKey=" + db.hashKEY
    CheckValue=CheckValue.encode('utf-8')
    hash_object = hashlib.sha256(CheckValue)
    hex_dig = hash_object.hexdigest()
    return hex_dig.upper()

@csrf_exempt
def CustomerURL(request):
    if request.method=="POST":
        form = CustomerUrlResponse(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponse()


class Test(UserBase):
    def get(self, request, *args, **kwargs):
        if kwargs['method']=="1":
            self.template_name = 'pay2go/test.html' # xxxx/xxx.html
            self.page_title = 'Customer' # title
            kwargs['form'] = CustomerUrlResponse()
        else:
            self.template_name = 'pay2go/test2.html' # xxxx/xxx.html
            self.page_title = 'Notify' # title
            kwargs['form'] = NotifyUrlResponse()
        
        
        
        return super(Test, self).get(request, *args, **kwargs)

class Pay2go(UserBase):
    template_name = 'pay2go/pay2go.html' # xxxx/xxx.html
    page_title = '付款' # title

    def get(self, request, *args, **kwargs):
        kwargs['dataError'] = True
        if not 'groupID' in kwargs:
            return super(Pay2go, self).get(request, *args, **kwargs)
        
        group = GroupOrder.objects.get(id=kwargs['groupID'])
        orderID = timeFormat(group.date)+str(group.id)
        pay = CustomerUrlDB.objects.filter(MerchantOrderNo=orderID)

        if len(pay)>0:
                return super(Pay2go, self).get(request, *args, **kwargs)
            
        MerchantOrderNo = "TESTNUMBER" + orderID
        Amt = str(group.totalAmount)
        Email = request.user.email
        ItemDesc = "123"
        data = BuyData(MerchantOrderNo, Amt, Email, ItemDesc, self.getHost(request))
        kwargs['BuyData'] = data
        kwargs['dataError'] = False

        
        
        return super(Pay2go, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super(Pay2go, self).post(request, *args, **kwargs)

def pay2go(request):
    template = 'pay2go/pay2go.html'
    
    if request.method=="GET":
        return render(request, template, {})
    
    form = BuyForm(request.POST)

    
    if not form.is_valid():
        return render(request, template, {})
    
    MerchantOrderNo = "TESTNUMBER" + form.cleaned_data['OrderNumber']
    Amt = form.cleaned_data['cost']
    Email = form.cleaned_data['email']
    ItemDesc = "測試物品"
    data = BuyData(MerchantOrderNo, Amt, Email, ItemDesc, "")
    return render(request, template, {"BuyData":data})
    
    
class BuyData:
    def __init__(self, MerchantOrderNo, Amt, Email, ItemDesc, host):
        TimeStamp = timeFormat(time())
        self.getDB()
        if self.isTest:
            MerchantOrderNo="TESTORDER"+MerchantOrderNo
            #self.postUrl="https://capi.pay2go.com/MPG/mpg_gateway"
            self.NotifyURL="https://"+host+"/pay2go/NotifyURL"
            self.CustomerURL="https://"+host+"/pay2go/CustomerURL"
        else:
            #self.postUrl="https://api.pay2go.com/MPG/mpg_gateway"
            self.NotifyURL="https://"+host+"/pay2go/NotifyURL"
            self.CustomerURL="https://"+host+"/pay2go/CustomerURL"

        self.postUrl="http://capi.pay2go.com/MPG/mpg_gateway" #test server
        
        self.MerchantID = self.memberID
        self.RespondType = "String"
        self.TimeStamp = TimeStamp
        self.Version = "1.1"
        self.MerchantOrderNo = MerchantOrderNo
        self.Amt = Amt
        self.ItemDesc = ItemDesc
        self.ExpireDate = ""
        self.ReturnURL = ""
        self.Email = Email
        self.LoginType = "0"
        self.CREDIT = "0"
        
        self.CheckValue = self.CreateCheckCode(Amt, MerchantOrderNo, TimeStamp)
        
    def getDB(self):
        db = setting()
        self.memberID = db.memberID
        self.hashKEY = db.hashKEY
        self.hashIV = db.hashIV
        self.enable = db.isActive
        self.isTest = db.isTest
        
    def CreateCheckCode(self, Amt, MerchantOrderNo, TimeStamp):
        CheckValue = "HashKey=" + self.hashKEY
        CheckValue+= "&Amt=" + Amt
        CheckValue+= "&MerchantID=" + self.memberID
        CheckValue+= "&MerchantOrderNo=" + MerchantOrderNo
        CheckValue+= "&TimeStamp=" + TimeStamp
        CheckValue+= "&Version=" + self.Version
        CheckValue+= "&HashIV=" + self.hashIV
        CheckValue=CheckValue.encode('utf-8')
        hash_object = hashlib.sha256(CheckValue)
        hex_dig = hash_object.hexdigest()
        return hex_dig.upper()
