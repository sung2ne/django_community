import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import SafeString

# 회원가입
class CustomUserCreationForm(UserCreationForm):    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='mb-3'>"))
            
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "email"]
    
    # 아이디 중복 확인
    def clean_username(self):
        username = self.cleaned_data.get("username")
        exist_username = User.objects.filter(username=username)
        if exist_username:
            raise forms.ValidationError("이미 사용중인 아이디입니다.")
        return username    
    
    # 이메일 중복 확인
    def clean_email(self):
        email = self.cleaned_data.get("email")
        exist_username = User.objects.filter(email=email)
        if exist_username:
            raise forms.ValidationError("이미 사용중인 이메일입니다.")
        return email
        
    username = forms.CharField(label="아이디")
    password1 = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    password2 = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput)
    first_name = forms.CharField(label="이름")
    email = forms.EmailField(label="이메일")