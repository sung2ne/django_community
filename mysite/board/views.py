from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from board.models import Board

# 목록, /board/
def board_list(request):
    # 페이지 번호
    page = request.GET.get("page", 1)
    
    # 목록
    b_list = Board.objects.all().order_by("-created_at")
    
    # 한페이지에 10개씩 보여주기
    paginator = Paginator(b_list, 10)
    page_obj = paginator.get_page(page)
    
    context = {
        "board_list": page_obj,
    }
    return render(request, "board/list.html", context)
