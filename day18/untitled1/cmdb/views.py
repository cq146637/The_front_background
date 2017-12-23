from django.shortcuts import render
import os
from django.views import View
from cmdb import models

# Create your views here.


from django.shortcuts import HttpResponse
from django.shortcuts import render   #封装了文件操作
from django.shortcuts import redirect   #封装了跳转操作

class Foo():
    def render(self):
        return HttpResponse("<h1>readding a book!!</h1>")
def read(request):
    response = HttpResponse("<h1>readding a book!!</h1>")
    return Foo()

def login(request):
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get("user", None)
        pwd = request.POST.get("pwd", None)
        # obj = models.UserInfo.objects.filter(username=user).first()
        # print(obj)
        # obj = models.UserInfo.objects.filter(username=user,pwd=pwd).count()
        if user=="root"and pwd=="123":
            return redirect("/cmdb/home")
        else:
            error_msg = "用户名或者密码错误"
    print(error_msg)
    return render(request,"login.html", {"error_msg": error_msg})

def home(request):
    USERS_LIST = [
        {"username":"刘磊","email":"liulei@qq.com","gender":"男"},
        {"username":"安光","email":"anguang@qq.com","gender":"男"},
        {"username":"超军","email":"chaojun@qq.com","gender":"男"},
        {"username":"广为","email":"guanwei@qq.com","gender":"男"},
    ]
    if request.method == "POST":
        u = request.POST.get("username",None)
        e = request.POST.get("email",None)
        g = request.POST.get("gender",None)
        print(u,e,g)
        user = {"username":u,"email":e,"gender":g}
        USERS_LIST.append(user)
    return render(request,"home.html",{"USERS_LIST": USERS_LIST})

def register(request):
    if request.method =="GET":
        return render(request, "register.html")
    if request.method == "POST":
        # u = request.POST.get("username",None)
        # e = request.POST.get("passwd",None)
        # g = request.POST.get("gender",None)
        # g = request.POST.get("favor",None)
        # g = request.POST.get("city",None)
        obj = request.FILES.get("file")
        FILE_PATH = os.path.join("uploda",obj.name)
        f = open(FILE_PATH,mode="wb")
        for i in obj.chunks():
            f.write(i)
        f.close()
    return render(request,"home.html")


class Register(View):

    def dispatch(self, request, *args, **kwargs):
        #CBV方式CBV方式CBV方式CBV方式CBV方式CBV方式CBV方式CBV方式
        #为了不直接进行GET，POST，方法，所以要重写dispatch方法，
        #但又不想失去原来的特性，所以调用父类原生的dispatch
        # ................定制功能加入
        result = super(Register,self).dispatch(request, *args, **kwargs)
        #................功能加入
        return result#在此基础上不改变原来的执行结果，还能加入自己的功能
    def get(self,requset):
        return render(requset, "register.html")

    def post(self,request):
        if request.method == "POST":
            # u = request.POST.get("username",None)
            # e = request.POST.get("passwd",None)
            # g = request.POST.get("gender",None)
            # g = request.POST.get("favor",None)
            # g = request.POST.get("city",None)
            # obj = request.FILES.get("file")
            # FILE_PATH = os.path.join("uploda", obj.name)
            # f = open(FILE_PATH, mode="wb")
            # for i in obj.chunks():
            #     f.write(i)
            # f.close()
            return render(request, "home.html")


def orm(request):
# models.UserInfo.objects.create(username='root',pwd='123')
# dic = {'username': 'eric', 'password': '666'}
# models.UserInfo.objects.create(**dic)

# obj = models.UserInfo(username='alex',password='123')
# obj.save()
#     result = models.UserInfo.objects.all()
    result = models.UserInfo.objects.filter(id=4)
    # result = models.UserInfo.objects.get(id=4)如果没此ＩＤ直接报错，只取一条
    # models.UserInfo.objects.filter(id=4).delete()
    # models.UserInfo.objects.filter(id=4).update(username=eric)

    for i in result:
        print(i.id,i.username,i.pwd)
    return HttpResponse("orm")

def father(request):
    return render(request,"father.html")

def child(request):
    return render(request,"child.html")

def tpl(request):
    aname = "ASASASASASsfasfasfasf"
    return render(request,"tpl.html",{"aname":aname})

LIST = []
for i in range(1000):
    LIST.append(i)

from django.utils.safestring import mark_safe
def user_list(request):
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)
    start = (current_page-1)*10
    end = current_page*10
    data = LIST[start:end]
    all_count = len(LIST)
    count,yu = divmod(all_count,10)
    if yu:
        count += 1
    page_list = []
    start_count = 0
    end_count = 0
    page_size = 5
    if all_count < page_size:
        start_count = 1
        end_count = page_size
    else:
        if current_page< page_size/2 +1:
            start_count = 1
            end_count = page_size + 1
        elif count - current_page < page_size/2:
            start_count = count - page_size + 1
            end_count = count + 1
        else:
            start_count = current_page - page_size/2
            end_count = current_page + page_size/2 +1
    star_pg= '<a class="page" href="/cmdb/user_list/?p=%s">首页</a>' % (1)
    page_list.append(star_pg)
    if current_page == 1:
        prev_pg = '<a class="page" href="javacript:void(0)">上一页</a>'
    else:
        prev_pg = '<a class="page" href="/cmdb/user_list/?p=%s">上一页</a>' % (current_page-1)
    page_list.append(prev_pg)
    for i in range(int(start_count),int(end_count)):
        if i ==current_page:
            temp = '<a class="page active" href="/cmdb/user_list/?p=%s">%s</a>' % (i,i)
        else:
            temp = '<a class="page" href="/cmdb/user_list/?p=%s">%s</a>' % (i,i)
        page_list.append(temp)
    if current_page == count:
        next_pg = '<a class="page" href="javacript:void(0)">下一页</a>'
    else:
        next_pg = '<a class="page" href="/cmdb/user_list/?p=%s">下一页</a>' % (current_page+1)
    page_list.append(next_pg)
    end_pg = '<a class="page" href="/cmdb/user_list/?p=%s">尾页</a>' % (count)
    page_list.append(end_pg)
    page_str = "".join(page_list)
    page_str = mark_safe(page_str)
    return render(request,"user_list.html",{"li":data,"page_str":page_str,"count":count})

from django.views.decorators.cache import cache_page
@cache_page(10)
def cache(request):
    import time
    ctime = time.time()
    return render(request,'cache.html',{'ctime':ctime})


def img(request):
    f = open('static/2.png','rb')
    img = f.read()



from django import forms

class LoingForm(forms.Form):
    user = forms.CharField()

