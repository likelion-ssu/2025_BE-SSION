from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    return HttpResponse("<h1>Article 페이지입니다~</h1>")