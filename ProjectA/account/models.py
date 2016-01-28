from django.db import models
from django.contrib.auth.models import User
from shop.models import Item
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=30, unique=True)
    fullName = models.CharField(max_length=128)
    #website = models.URLField(blank=True)
    address = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    ip = models.CharField(max_length=15, blank=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.fullName + ' (' + self.user.username + ')'

class GroupOrder(models.Model):
    user = models.ForeignKey(User)
    totalAmount = models.IntegerField()
    paymentMethod = models.IntegerField()
    paymentStatus = models.IntegerField()
    payerName = models.CharField(max_length=128)
    payerAddress = models.CharField(max_length=128)
    payerPhone = models.CharField(max_length=128)
    recipientName = models.CharField(max_length=128)
    recipientAddress = models.CharField(max_length=128)
    recipientPhone = models.CharField(max_length=128)
    recipientStatus = models.IntegerField()
    
    def __str__(self):
        return self.id + " (" + self.user.userprofile.fullName + ")"
    
class Order(models.Model):
    groupID = models.ForeignKey(GroupOrder)
    itemID = models.CharField(max_length=128)
    itemNmae = models.CharField(max_length=128)
    itemPrice = models.CharField(max_length=128)
    itemQty = models.IntegerField()
    def __str__(self):
        return self.itemID.name + " (所屬訂單 " + self.groupID + ")"
    
class MyCart(models.Model):
    user = models.ForeignKey(User)
    itemID = models.ForeignKey(Item)
    Qty = models.IntegerField()
    def __str__(self):
        return self.itemID.name + " ("+ self.user.username +")"
    
