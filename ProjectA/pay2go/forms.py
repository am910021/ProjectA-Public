# -*- coding: utf-8 -*-
from django import forms
from .models import NotifyDB, CustomerDB


class CustomerResponse(forms.ModelForm):
    class Meta:
        model = CustomerDB
        exclude = ("group", )
    
class NotifyResponse(forms.ModelForm):
    class Meta:
        model = NotifyDB
        exclude = ("group", )
        
