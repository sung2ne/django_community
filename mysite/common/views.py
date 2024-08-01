from django.http import HttpResponse
from django.shortcuts import redirect, render
from common.forms import LoginForm, RegisterForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password


# 메인 화면
def main_page(request):
    context = {}
    return render(request, "common/main.html", context)
    
# /common/login/
def common_login(request):
    # 템플릿으로 넘겨줄 정보
    context = {}
        
    if request.method == "POST":
        # 로그인 폼
        form = LoginForm(request.POST)
        
        # 넘어온 값 검증
        if form.is_valid():
            login_cd = form.cleaned_data
            
            # 아이디에 해당하는 사용자 정보 조회
            user = authenticate(request, username=login_cd["username"], password=login_cd["password"])
            
            # 사용자 유무 확인    
            if user is None:
                context["form"] = form
                context["error_message"] = "아이디를 확인하세요."
                return render(request, "common/login.html", context)
                
            # 비밀번호 검증
            if not user.is_authenticated:
                context["form"] = form
                context["error_message"] = "비밀번호를 확인하세요."
                return render(request, "common/login.html", context)
        
            # 메인 화면으로 이동
            return redirect("main_page")
        else:
            context["form"] = form
            context["error_message"] = "입력정보를 확인하세요."
            return render(request, "common/login.html", context)
        
    # 로그인 폼
    form = LoginForm()
    context["form"] = form
    return render(request, "common/login.html", context)
    
# /common/logout/
def common_logout(request):
    logout(request)
    return redirect("main_page")
    
# /common/profile/
def common_profile(request):
    return HttpResponse('/common/profile/')
    
# /common/password/
def common_password(request):
    return HttpResponse('/common/password/')    
    
# /common/register/
def common_register(request):
    # 템플릿으로 넘겨줄 정보
    context = {}
        
    if request.method == "POST":
        # 회원가입 폼
        form = RegisterForm(request.POST)
        
        # 넘어온 값 검증
        if form.is_valid():
            register_cd = form.cleaned_data
            
            # 아이디에 해당하는 사용자 정보 조회
            user = User.objects.filter(username=register_cd["username"])
            
            # 사용자 유무 확인    
            if user is None:
                context["form"] = form
                context["error_message"] = "사용중인 아이디입니다."
                return render(request, "common/register.html", context)
            
            # DB에 사용자 정보 등록
            user = User.objects.create(
                username=register_cd["username"], 
                password=make_password(register_cd["username"]), 
                first_name=register_cd["first_name"],
                email=register_cd["email"]
            )
            
            context["message"] = "사용자를 추가하였습니다."
            return render(request, "common/register.html", context)
        else:
            context["form"] = form
            context["error_message"] = "입력정보를 확인하세요."
            return render(request, "common/register.html", context)
        
    # 회원가입 폼
    form = RegisterForm()
    context["form"] = form
    return render(request, "common/register.html", context)
    
# /common/find_username/
def common_find_username(request):
    return HttpResponse('/common/find_username/')
    
# /common/reset_password/
def common_reset_password(request):
    return HttpResponse('/common/reset_password/')
