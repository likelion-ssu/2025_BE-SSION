from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def followRequest(request):
    return HttpResponse("<h1>팔로우 요청 페이지입니다.</h1>")

def followAccept(request):
    return HttpResponse("<h1>팔로우 승인 페이지입니다.</h1>")

def followIgnore(request):
    return HttpResponse("<h1>팔로우 무시 페이지입니다.</h1>")

def findFollow(request):
    return HttpResponse("<h1>팔로우 조회 페이지입니다.</h1>")