# -*- coding: utf-8 -*-
from django import forms
from .models import NotifyUrlDB, CustomerUrlDB

class BuyForm(forms.Form):
    OrderNumber = forms.CharField(required=True, initial="00000001")
    cost  = forms.CharField(required=True)
    email = forms.EmailField(required=True, initial="am910021@gmail.com")
    
class NotifyUrlResponse(forms.ModelForm):
    class Meta:
        model = NotifyUrlDB
        fields = '__all__'
        
        
class CustomerUrlResponse(forms.ModelForm):
    class Meta:
        model = CustomerUrlDB
        fields = '__all__'
