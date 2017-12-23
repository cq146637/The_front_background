from django.conf.urls import url, include
from django.contrib import admin
from scan import views

urlpatterns = [

    url(r'^add/$', views.add),
    # url(r'^read/', views.read),
    # url(r'^login', views.login),
    # url(r'^orm', views.orm),
    # url(r'^home', views.home),
    # url(r'^register', views.Register.as_view()),
    # url(r'^father', views.father),
    # url(r'^child', views.child),
    # url(r'^tpl', views.tpl),
    # url(r'^user_list', views.user_list),
    # url(r'^cache', views.cache),
    # url(r'^img/', views.img),
    # # url(r'^aaa-(?P<uid>\d+)-(?P<pid>\d+).html', views.aaa),
]