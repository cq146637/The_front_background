"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from website import views

urlpatterns = [
    url(r'^orm/', views.orm),
    url(r'^home/', views.home),
    url(r'^pages/', views.pages),
    url(r'^login/$', views.login),
    url(r'^login2/$', views.login),
    # url(r'^login', views.login),
    # url(r'^home', views.home),
    # url(r'^register', views.Register.as_view()),
    # url(r'^aaa-(?P<uid>\d+)-(?P<pid>\d+).html', views.aaa),
]