from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from website import models
from utils.page_make import Page
# Create your views here.

def orm(request):
    models.UserInfo.objects.create(username="chenqian",password="123")
    models.UserInfo.objects.create(username="zhangguanwei",password="123")
    return HttpResponse("<h1>OK!</h1>")


def home(request):
    # cookies = request.COOKIES.get('username')
    # if not cookies:
    #     return redirect('/a/login')
    # if cookies=='wode':
        return render(request,'myself.html')
    # else:
    #     return redirect('/a/login')


List = ['小男孩%s'%(i) for i in range(1,1001)]

def pages(request):
    request_page = int(request.GET.get("pid",1))
    every_page_count = int(request.COOKIES.get('every_page_count',10))
    page_obj = Page(request_page, len(List), request.path_info, every_page_count)  # 页对象
    # list = ['小男孩%s'%(i) for i in range((request_page-1)*10,request_page*10)]
    #上一种方法影响效率
    list = List[page_obj.start():page_obj.end()]                            #提取展示信息
    page_str = page_obj.page_str()                                          #获取HTML标签
    response =  render(request,'page.html',{'list':list,'page_str':page_str,'path_info':request.path_info})
    return response

def login(request):
    if request.method == 'GET':
        return render(request,'login_cookie.html')
    if request.method == 'POST':
        u = request.POST.get('username',None)
        p = request.POST.get('password',None)
        if u=='wode' and p=='123':
            response = redirect('/a/pages')
            response.set_cookie('username',u,max_age=60)
            return response
        else:
            return redirect('/a/login')

def login2(request):
    if request.method == 'GET':
        return render(request,'login_session.html')
    if request.method == 'POST':
        u = request.POST.get('username',None)
        p = request.POST.get('password',None)
        if u=='wode' and p=='123':
            response = redirect('/a/pages')
            return response
        else:
            return redirect('/a/login')

def index2(request):
    return HttpResponse('OK')
