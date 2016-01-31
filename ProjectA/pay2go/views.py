# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse,redirect
from .forms import BuyForm, NotifyUrlResponse, CustomerUrlResponse
import hashlib
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from main.models import Setting

class setting:
    def __init__(self):
        set = Setting.objects.get_or_create(name="pay2go")
        self.memberID = set.c1
        self.hashKEY = set.c2
        self.hashIV = set.c3
        self.enable = set.c4
        self.date = set.c5

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
            if CheckCode(Amt, MerchantOrderNo, TradeNo)==form.cleaned_data['CheckCode']:
                form.save()
    return HttpResponse()

def CheckCode(MerchantID, Amt, MerchantOrderNo, TradeNo):
    db = setting()
    CheckValue = "HashIV=" + db.hashIV
    CheckValue+= "&Amt=" + str(Amt)
    CheckValue+= "&MerchantID=" + MerchantID
    CheckValue+= "&MerchantOrderNo=" + MerchantOrderNo
    CheckValue+= "&TradeNo=" + TradeNo
    CheckValue+= "&HashKey=" + db.hashKEY
    
    hash_object = hashlib.sha256(CheckValue)
    hex_dig = hash_object.hexdigest()
    return hex_dig.upper()

@csrf_exempt
def CustomerURL(request):
    if request.method=="POST":
        form = CustomerUrlResponse(request.POST)
        if form.is_valid():
            form.save()
    #data = getDATA(request.POST)
    return HttpResponse()

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
    data = BuyData(MerchantOrderNo, Amt, Email, ItemDesc)
    return render(request, template, {"BuyData":data})
    
    
class BuyData:
    def __init__(self, MerchantOrderNo, Amt, Email, ItemDesc):
        self.getDB()
        TimeStamp = datetime.strftime(time(), '%Y%m%d')

        self.MerchantID = self.memberID
        self.RespondType = "String"
        self.TimeStamp = TimeStamp
        self.Version = "1.1"
        self.MerchantOrderNo = MerchantOrderNo
        self.Amt = Amt
        self.ItemDesc = ItemDesc
        self.ExpireDate = ""
        self.ReturnURL = ""
        self.NotifyURL = "https://philipb-pay2go.appspot.com/pay2go/NotifyURL"
        self.CustomerURL = "https://philipb-pay2go.appspot.com/pay2go/CustomerURL"
        self.Email = Email
        self.LoginType = "0"
        self.CREDIT = "0"
        
        self.CheckValue = self.CreateCheckCode(Amt, MerchantOrderNo, TimeStamp)
        
    def getDB(self):
        db = setting()
        self.memberID = db.memberID
        self.hashKEY = db.hashKEY
        self.hashIV = db.hashIV
        self.enable = db.getEnable()
        
    def CreateCheckCode(self, Amt, MerchantOrderNo, TimeStamp):
        CheckValue = "HashKey=" + self.hashKEY
        CheckValue+= "&Amt=" + Amt
        CheckValue+= "&MerchantID=" + self.memberID
        CheckValue+= "&MerchantOrderNo=" + MerchantOrderNo
        CheckValue+= "&TimeStamp=" + TimeStamp
        CheckValue+= "&Version=" + self.Version
        CheckValue+= "&HashIV=" + self.hashIV
        hash_object = hashlib.sha256(CheckValue)
        hex_dig = hash_object.hexdigest()
        return hex_dig.upper()
