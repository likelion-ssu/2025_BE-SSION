from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def write(request):
    return HttpResponse("<h1>게시글 작성 페이지입니다.</h1>")

def edit(request):
    return HttpResponse("<h1>게시글 수정 페이지입니다.</h1>")