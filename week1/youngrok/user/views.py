from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(requeset):
    return HttpResponse("<h1>로그인!</h1>")

def signup(request):
    return HttpResponse("<h1>회원가입!</h1>")

def logout(request):
    return HttpResponse("<h2>로그아웃!</h2>")