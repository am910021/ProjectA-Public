from django import forms
from shop.models import Brand

class BrandForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    name.widget.attrs.update({'class':'form-control'})
    description = forms.CharField(max_length=100)
    description.widget.attrs.update({'class':'form-control'})
    image = forms.ImageField(required=False)
    content = forms.CharField( widget=forms.Textarea )
    is_active = forms.BooleanField(label=("啟用"), required=False)
    is_active.initial=True
    
    class Meta:
        model = Brand
        fields = ('name', 'content', 'description','is_active')