from django.db import models
from django.contrib.auth.models import User
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
