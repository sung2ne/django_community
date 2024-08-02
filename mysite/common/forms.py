from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import SafeString

# 로그인
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        labels = {
            "username": "아이디",
            "password": "비밀번호",
        }
        help_texts = {
            "username": None,
            "password": None,
        }
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }

# 회원가입
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "email"]
        labels = {
            "username": "아이디",
            "password": "비밀번호",
            "first_name": "이름",
            "email": "이메일",
        }
        help_texts = {
            "username": None,
            "password": None,
            "first_name": None,
            "email": None,
        }
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

# 아이디 찾기
class FindUsernameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FindUsernameForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='mb-3'>"))
            
    class Meta:
        model = User
        fields = ["first_name", "email"]
        labels = {
            "first_name": "이름",
            "email": "이메일",
        }
        help_texts = {
            "first_name": None,
            "email": None,
        }
        """
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }
        """
