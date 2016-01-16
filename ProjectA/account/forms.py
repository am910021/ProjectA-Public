from django import forms
from django.contrib.auth.models import User
from account.models import UserProfile
from captcha import fields

class SignupForm(forms.ModelForm):
    username = forms.CharField(label='帳號')
    username.widget.attrs.update({'class':'form-control'})                    
    password = forms.CharField(widget=forms.PasswordInput(), label='密碼')
    password.widget.attrs.update({'class':'form-control'})                    
    password2 = forms.CharField(widget=forms.PasswordInput(), label='確認密碼')
    password2.widget.attrs.update({'class':'form-control'})
    email = forms.EmailField(label='電子郵件')
    email.widget.attrs.update({'class':'form-control'}) 
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password!=password2:
            raise forms.ValidationError('密碼不相符')
        return password2
    
    
class UserForm(forms.ModelForm):
    username = forms.CharField(label='帳號')
    username.widget.attrs.update({'class':'form-control', 'readonly':'readonly'})             
    password = forms.CharField(widget=forms.PasswordInput(), label='密碼', required=False)
    password.widget.attrs.update({'class':'form-control'})                    
    password2 = forms.CharField(widget=forms.PasswordInput(), label='確認密碼', required=False)
    password2.widget.attrs.update({'class':'form-control'})
    email = forms.EmailField(label='電子郵件')
    email.widget.attrs.update({'class':'form-control'}) 
    
    class Meta:
        model = User
        fields = ('username', 'email')
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('會員帳號不在')
        return username

class UserProfileForm(forms.ModelForm):
    fullName = forms.CharField(max_length=128, label='姓名', required=False)
    fullName.widget.attrs.update({'class':'form-control'}) 
    phone = forms.CharField(max_length=15, label='電話', required=False)
    phone.widget.attrs.update({'class':'form-control'}) 
    address = forms.CharField(max_length=128, label='地址', required=False)
    address.widget.attrs.update({'class':'form-control'}) 
    
    class Meta:
        model = UserProfile
        fields = ('fullName', 'phone', 'address')
        
class CaptchaForm(forms.Form):
    captcha = fields.ReCaptchaField(attrs={'lang': 'zh-TW'})