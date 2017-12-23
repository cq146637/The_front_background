from django.shortcuts import render,HttpResponse
from scanner import models
from utils.page_make import Page
import json
# Create your views here.


def add(request):
    if request.method == "GET":
        return  render(request,"scanner_website/add.html")
    if request.method =="POST":
        dic = {}
        dic["name"] = request.POST.get("name",None)
        dic["url"] = str(request.POST.get("url",None))
        dic["types_id"] = str(request.POST.get("types",None))
        if not models.website.objects.filter(**dic).first():
            models.website.objects.create(**dic)

        return render(request, "scanner_website/add.html")


def home(request):
    if request.method == "GET":
        return render(request,"home.html")


def website_show(request):
    request_page = int(request.GET.get("pid",1))
    every_page_count = int(request.COOKIES.get('every_page_count',5))
    website_list = []
    count = models.website.objects.all().select_related('types')
    for i in count:
        website_list.append(i)
    page_obj = Page(request_page, len(website_list), request.path_info, every_page_count)
    list = website_list[page_obj.start():page_obj.end()]                            #提取展示信息
    page_str = page_obj.page_str()                                          #获取HTML标签
    response =  render(request,'websiteShow.html',{'list':list,'page_str':page_str,'path_info':request.path_info})
    return response


def website_edit1(request):
    if request.method == "GET":
        webstie_list = models.website.objects.all()
        return  render(request,"websiteEdit1.html",{"list":webstie_list})

def website_edit2(request):
    if request.method == "GET":
        org_list = models.type.objects.all()
        return  render(request,"websiteEdit2.html",{"list":org_list})



def website_search(request):
    if request.method == "GET":
        type_list = models.type.objects.all()
        return render(request,"websiteSearch.html",{"type_list":type_list})


def website_search_filter(request,**kwargs):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        condition = {}
        name = request.POST.get("name",None)
        if name:
            condition['name__icontains'] = name
        url = request.POST.get("url",None)
        if url:
            condition['url__icontains'] = url
        for k,v in kwargs.items():
            if v==0:
                pass
            else:
                condition[k] = v
        tuple_list = models.website.objects.filter(**condition).values()
        data = []
        for k in tuple_list:
            data.append(k)
        return HttpResponse(json.dumps(data))
