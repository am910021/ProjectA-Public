from django.db import models
from datetime import datetime

# Create your models here.
class Type(models.Model):
    number = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128)
    Image = models.CharField(max_length=128)

    def __str__(self):
        return self.name + '(' + self.number + ')'
    
    def getValue(self):
        return self.id
    

class Item(models.Model):
    type = models.OneToOneField(Type)
    number = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128)
    cost = models.IntegerField()
    image = models.CharField(max_length=128)
    image2 = models.CharField(max_length=128)
    intro = models.TextField()
    ingredient = models.TextField()
    manual = models.TextField()
    enable = models.BooleanField(default=True)
    sp = models.BooleanField(default=False)
    new = models.BooleanField(default=True)
    time = models.DateTimeField()
    
    def __str__(self):
        return self.name + '(' + self.number + ')'
    

