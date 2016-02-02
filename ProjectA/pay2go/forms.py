# -*- coding: utf-8 -*-
from django import forms
from .models import NotifyUrlDB, CustomerUrlDB


class CustomerUrlResponse(forms.ModelForm):
    class Meta:
        model = CustomerUrlDB
        fields = '__all__'
    
class NotifyUrlResponse(forms.ModelForm):
    class Meta:
        model = NotifyUrlDB
        fields = '__all__'
        
