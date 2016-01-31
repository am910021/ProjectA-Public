from django.db import models

# Create your models here. 
class CustomerUrlDB(models.Model):
    Status          = models.CharField(max_length=10)
    Message         = models.CharField(max_length=50)
    MerchantID      = models.CharField(max_length=15)
    Amt             = models.IntegerField()
    TradeNo         = models.CharField(max_length=20)
    MerchantOrderNo = models.CharField(max_length=20)
    PaymentType     = models.CharField(max_length=10)
    CheckCode       = models.CharField(max_length=128)
    ExpireDate      = models.CharField(max_length=128)
    BankCode        = models.CharField(max_length=128, blank=True)
    CodeNo          = models.CharField(max_length=128, blank=True)
    Barcode_1       = models.CharField(max_length=128, blank=True)
    Barcode_2       = models.CharField(max_length=128, blank=True)
    Barcode_3       = models.CharField(max_length=128, blank=True)

    

class NotifyUrlDB(models.Model):
    Status              = models.CharField(max_length=10)
    Message             = models.CharField(max_length=50)
    MerchantID          = models.CharField(max_length=15)
    Amt                 = models.IntegerField()
    TradeNo             = models.CharField(max_length=20)
    MerchantOrderNo     = models.CharField(max_length=20)
    PaymentType         = models.CharField(max_length=10)
    RespondType         = models.CharField(max_length=10)
    CheckCode           = models.CharField(max_length=128)
    PayTime             = models.CharField(max_length=128)
    IP                  = models.CharField(max_length=15)
    EscrowBank          = models.CharField(max_length=10)
    TokenUseStatus      = models.IntegerField()
    RespondCode         = models.CharField(max_length=5)
    Auth                = models.CharField(max_length=6)
    Card6No             = models.CharField(max_length=6)
    Card4No             = models.CharField(max_length=4)
    Inst                = models.IntegerField()
    InstFirst           = models.IntegerField()
    InstEach            = models.IntegerField()
    ECI                 = models.CharField(max_length=2)
    PayBankCode         = models.CharField(max_length=10)
    PayerAccount5Code   = models.CharField(max_length=5)
    CodeNo              = models.CharField(max_length=30)
    Barcode_1           = models.CharField(max_length=20)
    Barcode_2           = models.CharField(max_length=20)
    Barcode_3           = models.CharField(max_length=20)

    #def put(self, *args, **kwargs):
    #    self.ID = self.key().id()
    #    if super(Order, self).put(*args, **kwargs):
    #        return True
    #    return False