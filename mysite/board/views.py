from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from board.models import Board

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
