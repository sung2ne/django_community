from django.http import HttpResponse
from django.shortcuts import render

# 목록, /board/
def board_list(request):
    return HttpResponse('/board/')
