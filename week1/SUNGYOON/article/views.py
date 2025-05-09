from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def picture(request):
    return HttpResponse("article picture")

def article_list(request):
    return HttpResponse("article list")