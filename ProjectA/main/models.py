from django.db import models
from _datetime import date

# Create your models here.

class Setting(models.Model):
    name = models.CharField(max_length=15, unique=True, blank=False)
    isActive = models.BooleanField(default=False)
    c1 = models.CharField(max_length=128, blank=True)
    c2 = models.CharField(max_length=128, blank=True)
    c3 = models.CharField(max_length=128, blank=True)
    c4 = models.CharField(max_length=128, blank=True)
    c5 = models.CharField(max_length=128, blank=True)
    c6 = models.CharField(max_length=128, blank=True)
    c7 = models.CharField(max_length=128, blank=True)
    c8 = models.CharField(max_length=128, blank=True)
    time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Notice(models.Model):
    title=models.CharField(max_length=128)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
class News(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date = models.DateTimeField()