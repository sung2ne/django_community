from django.http import HttpResponse
from django.shortcuts import redirect, render
from common.forms import FindUsernameForm, LoginForm, RegisterForm, ResetPasswordForm, ProfileForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password


# 메인 화면
def main_page(request):
    context = {}
    return render(request, "common/main.html", context)
    
# 로그인, /common/login/
def common_login(request):
    # 템플릿으로 넘겨줄 정보
    context = {}
        
    if request.method == "POST":
        # 로그인 폼
        form = LoginForm(request.POST)
        
        # 넘어온 값 검증
        if form.is_valid():
            cd = form.cleaned_data
            
            # 아이디에 해당하는 사용자 정보 조회
            user = authenticate(request, username=cd["username"], password=cd["password"])
            
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
            
            # 로그인 처리
            login(request, user)
        
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
    
# 로그아웃, /common/logout/
def common_logout(request):
    logout(request)
    return redirect("main_page")
    
# 프로필, /common/profile/
def common_profile(request):
    # 템플릿으로 넘겨줄 정보
    context = {}
        
    if request.method == "POST":
        # 정보 수정 폼
        form = ProfileForm(request.POST)
        
        # 넘어온 값 검증
        if form.is_valid():
            cd = form.cleaned_data
            
            # 사용자 정보 조회
            exist_users = User.objects.exclude(pk=request.user.pk).filter(email=cd["email"])
            
            # 사용자 유무 확인    
            if exist_users.exists():
                context["profile_form"] = form
                context["profile_error_message"] = "이미 등록된 이메일입니다."
                return render(request, "common/profile.html", context)
            
            # 사용자 정보 변경
            request.user.email = cd["email"]
            request.user.first_name = cd["first_name"]
            request.user.save()
            
            context["profile_form"] = form
            context["profile_success_message"] = "사용자 정보를 수정하였습니다."
            return render(request, "common/profile.html", context)
        
    # 정보 수정 폼
    form = ProfileForm()
    context["profile_form"] = form
    return render(request, "common/profile.html", context)
    
# 비밀번호 수정, /common/password/
def common_password(request):
    return HttpResponse('/common/password/')    
    
# 회원가입, /common/register/
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
            if user is not None:
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
            
            context["form"] = LoginForm()
            context["success_message"] = "사용자를 추가하였습니다. 로그인을 해주세요."
            return render(request, "common/login.html", context)
        
    # 회원가입 폼
    form = RegisterForm()
    context["form"] = form
    return render(request, "common/register.html", context)

# 아이디 찾기, /common/find_username
def common_find_username(request):
    # 템플릿으로 넘겨줄 정보
    context = {}
        
    if request.method == "POST":
        # 아이디 찾기 폼
        form = FindUsernameForm(request.POST)
        
        # 넘어온 값 검증
        if form.is_valid():
            cd = form.cleaned_data
            
            # 사용자 정보 조회
            user = User.objects.filter(first_name=cd["first_name"], email=cd["email"])
            
            # 사용자 유무 확인    
            if len(user) == 0:
                context["form"] = form
                context["error_message"] = "등록된 사용자가 없습니다."
                return render(request, "common/find_username.html", context)
            
            context["find_user"] = user[0]
            context["form"] = form
            context["success_message"] = "사용자를 찾았습니다."
            return render(request, "common/find_username.html", context)
        
    # 아이디 찾기 폼
    form = FindUsernameForm()
    context["form"] = form
    return render(request, "common/find_username.html", context)
    
# 비밀번호 초기화, /common/reset_password/
def common_reset_password(request):
    # 템플릿으로 넘겨줄 정보
    context = {}
        
    if request.method == "POST":
        # 비밀번호 초기화 폼
        form = ResetPasswordForm(request.POST)
        
        # 넘어온 값 검증
        if form.is_valid():
            cd = form.cleaned_data
            
            # 사용자 정보 조회
            user = User.objects.filter(username=cd["username"], first_name=cd["first_name"], email=cd["email"])
            
            # 사용자 유무 확인    
            if len(user) == 0:
                context["form"] = form
                context["error_message"] = "등록된 사용자가 없습니다."
                return render(request, "common/reset_password.html", context)
            
            # 비밀번호 초기화
            new_password = "1234"
            user[0].set_password(new_password)
            user[0].save()
            
            context["new_password"] = new_password
            context["form"] = form
            context["success_message"] = "비밀번호를 초기화했습니다."
            return render(request, "common/reset_password.html", context)
            
    # 비밀번호 초기화 폼
    form = ResetPasswordForm()
    context["form"] = form
    return render(request, "common/reset_password.html", context)
