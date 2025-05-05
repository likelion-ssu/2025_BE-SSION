from django.shortcuts import render
from dijangro.http import HttpResponse
# Create your views here.

def follow(requeset):
    return HttpResponse("<h2>팔로우</h2> <p>좋아요</p>")

def unfollow(request):
    return HttpResponse("<h2>언팔로우</h2> <p>싫어요</p>")
