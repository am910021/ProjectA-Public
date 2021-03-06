from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from shop.models import Item
# Create your models here.

def timeFormat(time):
    return str(datetime.strftime(time, '%Y%m%d'))

class Profile(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=30, unique=True)
    fullName = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    ip = models.CharField(max_length=15, blank=True)
    isVerified = models.BooleanField(default=False)
    regDate = models.DateTimeField(auto_now_add=True)
    changeDate = models.DateTimeField(auto_now=True)
    resetCode = models.CharField(max_length=15, blank=True)
    
    
    def __str__(self):
        return self.fullName + ' (' + self.user.username + ')'

class GroupOrder(models.Model):
    user = models.ForeignKey(User)
    number = models.CharField(max_length=128)
    totalAmount = models.IntegerField(default=0)
    paymentMethod = models.IntegerField(default=0)
    paymentStatus = models.IntegerField(default=0)
    payerName = models.CharField(max_length=128, blank=True)
    payerAddress = models.CharField(max_length=128, blank=True)
    payerPhone = models.CharField(max_length=128, blank=True)
    recipientName = models.CharField(max_length=128, blank=True)
    recipientAddress = models.CharField(max_length=128, blank=True)
    recipientPhone = models.CharField(max_length=128, blank=True)
    status = models.IntegerField(default=0)
    date = models.DateTimeField()
    num = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        self.date = timezone.now()
        orderID = timeFormat(self.date)+str(self.id)
        self.number = orderID[2:]
        super(GroupOrder, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.id) + " (" + self.user.username + ")"
    
class Order(models.Model):
    group = models.ForeignKey(GroupOrder)
    item = models.ForeignKey(Item)
    nmae = models.CharField(max_length=128)
    cost = models.IntegerField()
    qty = models.IntegerField()
    def __str__(self):
        return self.item.name + " ("+ str(self.id) +")"
    
class MyCart(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    qty = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.item.name + " ("+ self.user.username +")"
    
