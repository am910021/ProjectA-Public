from django import forms
from django.contrib.auth.models import User
from account.models import Profile, GroupOrder
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
    
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password!=password2:
            raise forms.ValidationError('密碼不相符')
        return password2

class ProfileForm(forms.ModelForm):
    fullName = forms.CharField(max_length=128, label='姓名', required=False)
    fullName.widget.attrs.update({'class':'form-control'}) 
    phone = forms.CharField(max_length=15, label='電話', required=False)
    phone.widget.attrs.update({'class':'form-control'}) 
    address = forms.CharField(max_length=128, label='地址', required=False)
    address.widget.attrs.update({'class':'form-control'}) 
    
    class Meta:
        model = Profile
        fields = ('fullName', 'phone', 'address')
        
class CheckOutForm(forms.Form):
    payerName = forms.CharField(max_length=128)
    payerName.widget.attrs.update({'class':'form-control'})
    payerAddress = forms.CharField(max_length=128)
    payerAddress.widget.attrs.update({'class':'form-control'})
    payerPhone = forms.CharField(max_length=128)
    payerPhone.widget.attrs.update({'class':'form-control'})
    recipientName = forms.CharField(max_length=128)
    recipientName.widget.attrs.update({'class':'form-control'})
    recipientAddress = forms.CharField(max_length=128)
    recipientAddress.widget.attrs.update({'class':'form-control'})
    recipientPhone = forms.CharField(max_length=128)
    recipientPhone.widget.attrs.update({'class':'form-control'})
    
    def setReadOnly(self):
        self.fields['payerName'].widget.attrs.update({'readonly':'readonly'})
        self.fields['payerAddress'].widget.attrs.update({'readonly':'readonly'})
        self.fields['payerPhone'].widget.attrs.update({'readonly':'readonly'})
        self.fields['recipientName'].widget.attrs.update({'readonly':'readonly'})
        self.fields['recipientAddress'].widget.attrs.update({'readonly':'readonly'})
        self.fields['recipientPhone'].widget.attrs.update({'readonly':'readonly'})
    
    def clean_payerPhone(self):
        payerPhone = self.cleaned_data.get('payerPhone')
        phone = payerPhone.replace("-","").replace("#","").replace("+","").replace(" ","")
        if not phone.isdigit():
            raise forms.ValidationError('電話格式錯誤（ex 01-23456789）')
        return payerPhone
    
    def clean_recipientPhone(self):
        recipientPhone = self.cleaned_data.get('recipientPhone')
        phone = recipientPhone.replace("-","").replace("#","").replace("+","").replace(" ","")
        if not phone.isdigit():
            raise forms.ValidationError('電話格式錯誤（ex 01-23456789）')
        return recipientPhone
    
class ResetPwd(forms.Form):
    username = forms.CharField()
    username.widget.attrs.update({'class':'form-control'})             
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    password.widget.attrs.update({'class':'form-control'})                    
    password2 = forms.CharField(widget=forms.PasswordInput(), required=False)
    password2.widget.attrs.update({'class':'form-control'})
    code = forms.CharField(label='重置碼')
    code.widget.attrs.update({'class':'form-control'}) 
     
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password!=password2:
            raise forms.ValidationError('密碼不相符')
        return password2
    
class CaptchaForm(forms.Form):
    captcha = fields.ReCaptchaField(attrs={'lang': 'zh-TW'})