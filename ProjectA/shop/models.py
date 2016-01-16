from django.db import models
from datetime import datetime

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
    brand = models.OneToOneField(Brand)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=128, blank=True)
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    

class Item(models.Model):
    category = models.OneToOneField(Category)
    number = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128)
    cost = models.IntegerField()
    image = models.CharField(max_length=128)
    image2 = models.CharField(max_length=128)
    intro = models.TextField()
    ingredient = models.TextField()
    manual = models.TextField()
    isActive = models.BooleanField(default=True)
    sp = models.BooleanField(default=False)
    new = models.BooleanField(default=True)
    time = models.DateTimeField()
    
    def __str__(self):
        return self.name + '(' + self.number + ')'
    

