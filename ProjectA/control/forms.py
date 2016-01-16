from django import forms
from shop.models import Brand, Category
from main.models import Setting

class BrandForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    name.widget.attrs.update({'class':'form-control required'})
    description = forms.CharField(max_length=100)
    description.widget.attrs.update({'class':'form-control'})
    image = forms.ImageField(required=False)
    content = forms.CharField( widget=forms.Textarea )
    content.widget.attrs.update({'class':'form-control required'})
    isActive = forms.BooleanField(label=("啟用"), required=False)
    isActive.initial=True
    
    class Meta:
        model = Brand
        fields = ('name', 'content', 'description','isActive')
        
        
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    name.widget.attrs.update({'class':'form-control'})
    description = forms.CharField(max_length=100)
    description.widget.attrs.update({'class':'form-control'})
    image = forms.ImageField(required=False)
    isActive = forms.BooleanField(label=("啟用"), required=False)
    isActive.initial=True
    
    class Meta:
        model = Category
        fields = ('name', 'description','isActive', 'brand')
        

class EnableCategory(forms.ModelForm):
    CHOICES=[('True','啟用'),
         ('False','停用')]
    
    name = forms.CharField(max_length=15, widget=forms.HiddenInput())
    isActive = forms.BooleanField()
    
    class Meta:
        model = Setting
        fields = ('name', 'isActive') 

    
    
    
    