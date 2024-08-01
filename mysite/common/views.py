from django.http import HttpResponse
from django.shortcuts import redirect, render


# 메인 화면
def main_page(request):
    context = {}
    return render(request, "common/main.html", context)
    
# /common/login/
def common_login(request):
    if request["method"] == "POST":
        # 넘어온 값 검증
        
        # 아이디에 해당하는 사용자 정보 조회

        # 사용자 유무 확인
        
        # 비밀번호 검증
        
        # 인증정보(세션) 생성
        
        return redirect("main_page")
        
    context = {}
    return render(request, "common/login.html", context)
    
# /common/logout/
def common_logout(request):
    return HttpResponse('/common/logout/')
    
# /common/profile/
def common_profile(request):
    return HttpResponse('/common/profile/')
    
# /common/password/
def common_password(request):
    return HttpResponse('/common/password/')    
    
# /common/register/
def common_register(request):
    return HttpResponse('/common/register/')
    
# /common/find_username/
def common_find_username(request):
    return HttpResponse('/common/find_username/')
    
# /common/reset_password/
def common_reset_password(request):
    return HttpResponse('/common/reset_password/')
