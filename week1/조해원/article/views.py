from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addArticle(request) :
    return HttpResponse("<h1>📝add article</h1>")
def checkArticle(request) :
    return HttpResponse("<h1>✔check article</h1>")
def likeArticle(request) :
    return HttpResponse("<h1>I like this article❤️</h1>")
def shareArticle(request) : 
    return HttpResponse("<h1>🛜share this article</h1>")
