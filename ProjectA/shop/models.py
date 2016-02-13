from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=128, blank=True)
    content = models.TextField(blank=True)
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    brand =  models.ForeignKey(Brand)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=128, blank=True)
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    

class Item(models.Model):
    category =  models.ForeignKey(Category)
    number = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128)
    cost = models.IntegerField()
    inventory = models.IntegerField()
    image = models.CharField(max_length=128, blank=True)
    image2 = models.CharField(max_length=128, blank=True)
    
    intro  = models.TextField(blank=True)
    introduction = models.TextField(blank=True)
    ingredient = models.TextField(blank=True)
    manual = models.TextField(blank=True)
    isActive = models.BooleanField(default=True)
    sp = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        shownumber = self.number if self.number!="" else "未設定編號"
        return self.name + ' (' + shownumber + ')'
    

