from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.contrib.auth import logout, authenticate, login
from board.models import Board
from board.forms import CreateForm

# 목록, /board/
def board_list(request):
    # 페이지 번호
    page = request.GET.get("page", 1)
    
    # 목록
    b_list = Board.objects.all().order_by("-created_at")
    
    # 검색
    kw = request.GET.get("kw", "")
    where = request.GET.get("where", "")
    
    if kw and where == "all":
        b_list = b_list.filter(
            Q(title__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) # 내용검색
        ).distinct()
    elif kw and where == "title":
        b_list = b_list.filter(
            Q(title__icontains=kw)
        ).distinct()
    elif kw and where == "content":
        b_list = b_list.filter(
            Q(content__icontains=kw)
        ).distinct()
    
    # 한페이지에 10개씩 보여주기
    paginator = Paginator(b_list, 10)
    page_obj = paginator.get_page(page)
    
    context = {
        "board_list": page_obj,
        "kw": kw,
        "where": where,
        "page": page,
    }
    return render(request, "board/list.html", context)


# 등록, /board/create/
def board_create(request):
    # 페이지 번호
    page = request.GET.get("page", 1)
    
    # 등록 폼   
    form = CreateForm()
    
    # 템플릿으로 넘겨줄 정보
    context = {
        "page": page,
        "form": form,
    }
    
    # POST
    if request.method == "POST":       
        # 등록 폼   
        form = CreateForm(request.POST)
        
        # 넘어온 값 검증
        if form.is_valid():
            cd = form.cleaned_data
            
            # 등록하기
            b = Board.objects.create(title=cd["title"], content=cd["content"], author=request.user)
            b.save()
            
            # 메시지
            messages.success(request, "게시글이 등록되었습니다.")
            
            # 목록으로 이동
            return redirect("board:read", b.id)    
    
    # 등록 화면
    return render(request, "board/create.html", context)

# 보기, /board/<board_id>/
def board_read(request, board_id):
    # 페이지 번호
    page = request.GET.get("page", 1)
    
    # 게시글
    b = get_object_or_404(Board, pk=board_id)
    
    context = {
        "page": page,
        "board": b,    
    }
    
    return render(request, "board/read.html", context)

# 삭제, /board/<board_id>/delete/
def board_delete(request, board_id):
    # 게시글
    b = get_object_or_404(Board, pk=board_id)
    
    # 삭제 권한 확인
    if request.user.username != b.author.username:
        logout(request)
        return redirect("main_page")
    
    # 삭제
    b.delete()
    
    # 메시지
    messages.success(request, "게시글이 삭제되었습니다.")
    
    # 목록으로 이동
    return redirect("board:list")