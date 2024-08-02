from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import SafeString

# 로그인
class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='mb-3'>"))
    
    username = forms.CharField(label="아이디")
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput())

# 회원가입
class RegisterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='mb-3'>"))
    
    username = forms.CharField(label="아이디")
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput())
    first_name = forms.CharField(label="이름")
    email = forms.EmailField(label="이메일")
        
# 아이디 찾기
class FindUsernameForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FindUsernameForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='mb-3'>"))
    
    first_name = forms.CharField(label="이름")
    email = forms.EmailField(label="이메일")

# 비밀번호 초기화
class ResetPasswordForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='mb-3'>"))
    
    username = forms.CharField(label="아이디")
    first_name = forms.CharField(label="이름")
    email = forms.EmailField(label="이메일")
    
# 정보 수정
class ProfileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='mb-3'>"))
    
    first_name = forms.CharField(label="이름")
    email = forms.EmailField(label="이메일")


# 비밀번호 수정
class PasswordForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='mb-3'>"))
    
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput())
    re_password = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput())
