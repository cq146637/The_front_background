from django.conf.urls import url, include
from django.contrib import admin
from scanner import views

urlpatterns = [
    url(r'^add/$', views.add),
    url(r'^home/$', views.home),
    url(r'^website/show/$', views.website_show),
    url(r'^website/edit1/$', views.website_edit1),
    url(r'^website/edit2/$', views.website_edit2),
    url(r'^website/search/$', views.website_search),
    url(r'^website/filter(?P<types_id>\d+).html$', views.website_search_filter),

    # url(r'^register', views.Register.as_view()),
    # # url(r'^aaa-(?P<uid>\d+)-(?P<pid>\d+).html', views.aaa),
]