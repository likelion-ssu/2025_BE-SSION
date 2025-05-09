from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request) :
    return HttpResponse("<h1>🙋‍♀️login please🙋‍♀️</h1>")
def register(request) :
    return HttpResponse("<h1>welcome, register complete❗️</h1>")
def editProfile(request) :
    return HttpResponse("<h1>edit your profile</h1>")