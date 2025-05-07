from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(requsest):
    return HttpResponse("<h1>This is article app.<h1/>")