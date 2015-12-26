from django.db import models

# Create your models here.
class Type(models.Model):
    number = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128)
    Image = models.CharField(max_length=128)

    def __str__(self):
        return self.name + '(' + self.number + ')'
    

class Item(models.Model):
    type = models.OneToOneField(Type)
    typeName = type.name
    number = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128)
    cost = models.IntegerField()
    image = models.CharField(max_length=128)
    image2 = models.CharField(max_length=128)
    intro = models.TextField()
    enable = models.CharField(max_length=128)
    sp = models.CharField(max_length=128)
    new = models.CharField(max_length=128)
    ingredient = models.TextField()
    manual = models.TextField()
    time = models.TimeField()
    
    def __str__(self):
        return self.name + '(' + self.number + ')'
    

