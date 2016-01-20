from django import forms
from shop.models import Brand, Category, Item
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
        
class ItemForm(forms.ModelForm):
    name = forms.CharField(max_length=128, label='商品名稱')
    name.widget.attrs.update({'class':'form-control'})
    cost = forms.IntegerField(label='商品價格')
    cost.widget.attrs.update({'class':'form-control'})
    inventory  = forms.IntegerField(label='商品庫存')
    inventory.widget.attrs.update({'class':'form-control'})
    inventory.initial = 10
    image = forms.ImageField(required=False, label='商品圖片')
    image2 = forms.ImageField(required=False, label='促銷, 新商品訊息圖片')
    
    intro  = forms.CharField( max_length=600, label='簡介')
    intro.widget.attrs.update({'class':'form-control'})
    introduction = forms.CharField( widget=forms.Textarea, label='介紹')
    ingredient = forms.CharField( widget=forms.Textarea, label='成份')
    manual = forms.CharField( widget=forms.Textarea, label='使用手冊')

    isActive = forms.BooleanField(label='啟用商品', required=False)
    isActive.initial=True
    sp = forms.BooleanField(label='促銷商品', required=False)
    sp.initial=False
    new = forms.BooleanField(label='新上架商品', required=False)
    new.initial=False
    
    """
    category = forms.ChoiceField(label=u'category')
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = [(e.id, e.name) for e in Category.objects.all()]
    """
    class Meta:
        model = Item
        exclude = ('number', 'image', 'image2', 'time')
        
    def clean_cost(self):
        cost = self.cleaned_data.get('cost')
        if cost<=0:
            raise forms.ValidationError('價錢過低。')
        return cost
