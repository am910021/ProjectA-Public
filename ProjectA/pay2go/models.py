from django.db import models
from account.models import GroupOrder

# Create your models here. 
class CustomerDB(models.Model):
    group = models.OneToOneField(GroupOrder)
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
    
    def save(self, *args, **kwargs):
        group = GroupOrder.objects.get(number=self.MerchantOrderNo)
        if group.paymentStatus<1:
            group.paymentStatus=1
            group.save()
        self.group = group
        super(CustomerDB, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.MerchantOrderNo
    

class NotifyDB(models.Model):
    group = models.OneToOneField(GroupOrder)
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
    EscrowBank          = models.CharField(max_length=10, blank=True)
    TokenUseStatus      = models.CharField(max_length=1, blank=True) #?
    
    RespondCode         = models.CharField(max_length=5, blank=True)
    Auth                = models.CharField(max_length=6, blank=True)
    Card6No             = models.CharField(max_length=6, blank=True)
    Card4No             = models.CharField(max_length=4, blank=True)
    Inst                = models.CharField(max_length=10, blank=True) #?
    InstFirst           = models.CharField(max_length=10, blank=True) #?
    InstEach            = models.CharField(max_length=10, blank=True) #?
    ECI                 = models.CharField(max_length=2, blank=True)
    
    PayBankCode         = models.CharField(max_length=10, blank=True)
    PayerAccount5Code   = models.CharField(max_length=5, blank=True)
    CodeNo              = models.CharField(max_length=30, blank=True)
    Barcode_1           = models.CharField(max_length=20, blank=True)
    Barcode_2           = models.CharField(max_length=20, blank=True)
    Barcode_3           = models.CharField(max_length=20, blank=True)
    
    def save(self, *args, **kwargs):
        group = GroupOrder.objects.get(number=self.MerchantOrderNo)
        if group.paymentStatus<2:
            group.paymentStatus=2
            group.save()
        self.group = group
        super(NotifyDB, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.MerchantOrderNo

    #def put(self, *args, **kwargs):
    #    self.ID = self.key().id()
    #    if super(Order, self).put(*args, **kwargs):
    #        return True
    #    return False