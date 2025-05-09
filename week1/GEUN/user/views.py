from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    return HttpResponse("""
        <h1>USER</h1>
        <ul>
            <li><a href="/user/login/">LOGIN</a></li>
            <li><a href="/user/register/">REGISTER</a></li>
        </ul>
    """)
def login(request):
    return HttpResponse("<h2>What's your username?<h2/>")
def register(request):
    return HttpResponse("<h2>Register into new account!<h2/>")