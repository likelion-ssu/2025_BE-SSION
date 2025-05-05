from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show(request):
    return HttpResponse("<h1>게시글</h1> <p>게시글 내용</p>")

def secret(requset):
    return HttpResponse("<h2>백엔드가 최고야</h2>")
