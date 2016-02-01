from django.db import models
from django.contrib.auth.models import User
from shop.models import Item
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=30, unique=True)
    fullName = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    ip = models.CharField(max_length=15, blank=True)
    isVerified = models.BooleanField(default=False)
    regDate = models.DateTimeField()
    changeDate = models.DateTimeField(auto_now=True)
    resetCode = models.CharField(max_length=15, blank=True)
    
    
    def __str__(self):
        return self.fullName + ' (' + self.user.username + ')'

class GroupOrder(models.Model):
    user = models.ForeignKey(User)
    totalAmount = models.IntegerField(default=0)
    paymentMethod = models.IntegerField(default=0)
    paymentStatus = models.IntegerField(default=0)
    payerName = models.CharField(max_length=128, blank=True)
    payerAddress = models.CharField(max_length=128, blank=True)
    payerPhone = models.CharField(max_length=128, blank=True)
    recipientName = models.CharField(max_length=128, blank=True)
    recipientAddress = models.CharField(max_length=128, blank=True)
    recipientPhone = models.CharField(max_length=128, blank=True)
    recipientStatus = models.IntegerField(default=0)
    date = models.DateTimeField()
    num = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id) + " (" + self.user.profile.fullName + ")"
    
class Order(models.Model):
    group = models.ForeignKey(GroupOrder)
    itemID = models.ForeignKey(Item)
    itemNmae = models.CharField(max_length=128)
    itemPrice = models.CharField(max_length=128)
    qty = models.IntegerField()
    def __str__(self):
        return self.itemID.name + " ("+ str(self.id) +")"
    
class MyCart(models.Model):
    user = models.ForeignKey(User)
    itemID = models.ForeignKey(Item)
    qty = models.IntegerField()
    date = models.DateTimeField()
    def __str__(self):
        return self.itemID.name + " ("+ self.user.username +")"
    
