"""
URL configuration for instaProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import display as display1
from user.views import login, register
from article.views import display as display2
from following.views import display as display3
from .views import mainPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainPage),
    path('user/', display1),
    path('article/', display2),
    path('following/', display3),
    path('user/login/', login),
    path('user/register/', register),
]
