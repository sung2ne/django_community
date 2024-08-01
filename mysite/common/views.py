from django.http import HttpResponse
from django.shortcuts import render

# /common/login/
def common_login(request):
    HttpResponse('/common/login/')
    
# /common/logout/
def common_logout(request):
    HttpResponse('/common/logout/')
    
# /common/profile/
def common_profile(request):
    HttpResponse('/common/profile/')
    
# /common/password/
def common_password(request):
    HttpResponse('/common/password/')    
    
# /common/register/
def common_register(request):
    HttpResponse('/common/register/')
    
# /common/find_username/
def common_find_username(request):
    HttpResponse('/common/find_username/')
    
# /common/reset_password/
def common_reset_password(request):
    HttpResponse('/common/reset_password/')
