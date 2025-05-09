from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signUp(request):
    return HttpResponse("<h1>회원가입 페이지입니다.</h1>")

def login(request):
    return HttpResponse("<h1>로그인 페이지입니다.</h1>")

def editProfile(request):
    return HttpResponse("<h1>프로필 편집 페이지입니다.</h1>")