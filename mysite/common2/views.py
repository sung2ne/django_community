from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.safestring import mark_safe
from common2.forms import CustomUserCreationForm

# 회원가입, /common2/register/
def common2_register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) 
        
        # 넘어온 값 검증
        if form.is_valid():
            # 사용자 등록
            user = form.save(commit=False)
            user.save()
            
            # 로그인 화면으로 이동
            messages.success(request, mark_safe("회원이 되신걸 환영합니다.<br>로그인을 진행해주세요."))
            redirect("common2:login")
    else:
        form = CustomUserCreationForm()
        
    context = {"form": form}
    return render(request, "common2/register.html", context)