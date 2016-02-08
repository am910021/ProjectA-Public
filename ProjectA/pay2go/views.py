from datetime import datetime, timedelta
import hashlib
from django.shortcuts import HttpResponse,redirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from main.models import Setting
from main.views import UserBase
from account.models import GroupOrder
from .forms import NotifyResponse, CustomerResponse


def time():
    return str(datetime.strftime(datetime.now()+ timedelta(hours=8), '%Y%m%d'))

def CheckCode(MerchantID, Amt, MerchantOrderNo, TradeNo):
    db = Pay2goData()
    CheckValue = "HashIV=" + db.hashIV
    CheckValue+= "&Amt=" + str(Amt)
    CheckValue+= "&MerchantID=" + MerchantID
    CheckValue+= "&MerchantOrderNo=" + MerchantOrderNo
    CheckValue+= "&TradeNo=" + TradeNo
    CheckValue+= "&HashKey=" + db.hashKEY
    CheckValue=CheckValue.encode('utf-8')
    hash_object = hashlib.sha256(CheckValue)
    hex_dig = hash_object.hexdigest()
    return hex_dig.upper()

@csrf_exempt
def NotifyURL(request):
    if request.method=="POST":
        form = NotifyResponse(request.POST)
        if form.is_valid():
            MerchantID = form.cleaned_data['MerchantID']
            Amt = form.cleaned_data['Amt']
            MerchantOrderNo = form.cleaned_data['MerchantOrderNo']
            TradeNo = form.cleaned_data['TradeNo']
            code = CheckCode(MerchantID, Amt, MerchantOrderNo, TradeNo)
            if code==form.cleaned_data['CheckCode']:
                form.save()
    return HttpResponse(request)

@csrf_exempt
def CustomerURL(request):
    if request.method=="POST":
        form = CustomerResponse(request.POST)
        if form.is_valid():
            MerchantID = form.cleaned_data['MerchantID']
            Amt = form.cleaned_data['Amt']
            MerchantOrderNo = form.cleaned_data['MerchantOrderNo']
            TradeNo = form.cleaned_data['TradeNo']
            code = CheckCode(MerchantID, Amt, MerchantOrderNo, TradeNo)
            if code==form.cleaned_data['CheckCode']:
                form.save()
    return HttpResponse()

class Pay2go(UserBase):
    template_name = 'pay2go/pay2go.html' # xxxx/xxx.html
    page_title = '付款' # title

    def get(self, request, *args, **kwargs):
        if not 'groupID' in kwargs:
            kwargs['status'] = "notfound"
            return super(Pay2go, self).get(request, *args, **kwargs)
        try:
            group = GroupOrder.objects.get(id=kwargs['groupID'])
        except Exception as e:
            kwargs['status'] = "notfound"
            return super(Pay2go, self).get(request, *args, **kwargs)
        
        if group.paymentStatus>0:
            kwargs['status'] = "paid"
            return super(Pay2go, self).get(request, *args, **kwargs)
        
        MerchantOrderNo = group.number
        Amt = str(group.totalAmount)
        Email = request.user.email
        ItemDesc = "商品"
        data = Pay2goData()
        data.create(MerchantOrderNo, Amt, Email, ItemDesc, self.getHost(request))
        kwargs['BuyData'] = data
        return super(Pay2go, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super(Pay2go, self).post(request, *args, **kwargs)

class Pay2goData:
    def __init__(self):
        set = Setting.objects.get(name="pay2go")
        self.memberID = set.c1
        self.hashKEY = set.c2
        self.hashIV = set.c3
        self.isTest = True if set.c4=="True" else False
        self.enable = set.isActive
        if self.memberID=="" or self.hashIV=="" or self.hashKEY=="":
            self.isActive = False

        
    def create(self, MerchantOrderNo, Amt, Email, ItemDesc, host):
        TimeStamp = time()
        if self.isTest:
            MerchantOrderNo=MerchantOrderNo #"TEST"+MerchantOrderNo
            self.postUrl="https://capi.pay2go.com/MPG/mpg_gateway"
            self.NotifyURL="http://"+host+"/pay2go/NotifyURL/"
            #self.CustomerURL="http://"+host+"/pay2go/CustomerURL/"
        else:
            self.postUrl="https://api.pay2go.com/MPG/mpg_gateway"
            self.NotifyURL="https://"+host+"/pay2go/NotifyURL"
            #self.CustomerURL="https://"+host+"/pay2go/CustomerURL/"
        
        self.MerchantID = self.memberID
        self.RespondType = "String"
        self.TimeStamp = TimeStamp
        self.Version = "1.1"
        self.MerchantOrderNo = MerchantOrderNo
        self.Amt = Amt
        self.ItemDesc = "["+settings.SITE_NAME+"]"+ ItemDesc
        self.ExpireDate = ""
        self.ReturnURL = ""
        self.Email = Email
        self.LoginType = "0"
        self.CREDIT = "0"
        self.CheckValue = self.CreateCheckCode(Amt, MerchantOrderNo, TimeStamp)
        
    def CreateCheckCode(self, Amt, MerchantOrderNo, TimeStamp):
        Value = "HashKey=" + self.hashKEY
        Value+= "&Amt=" + Amt
        Value+= "&MerchantID=" + self.memberID
        Value+= "&MerchantOrderNo=" + MerchantOrderNo
        Value+= "&TimeStamp=" + TimeStamp
        Value+= "&Version=" + self.Version
        Value+= "&HashIV=" + self.hashIV
        Value=Value.encode('utf-8')
        hash_object = hashlib.sha256(Value)
        hex_dig = hash_object.hexdigest()
        return hex_dig.upper()
    