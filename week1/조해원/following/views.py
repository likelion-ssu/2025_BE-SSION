from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def followRequest(request) :
    return HttpResponse("<h1>📥follow request</h1>")
def acceptFollow(request) :
    return HttpResponse("<h1>🙆‍♀️accept follow request</h1>")
def ignoreFollow(request) :
    return HttpResponse("<h1>🙅‍♀️ignore follow request</h1>")
def viewFollowRequest(request) : 
    return HttpResponse("<h1>👀view follow request</h1>")