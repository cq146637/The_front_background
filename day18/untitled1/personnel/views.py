from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request,'login3.html')
    if request.method == 'POST':
        if request.POST.get('username',None)=='redhat' and request.POST.get('password',None)=='123':
            request.session['is_login'] = True
            request.session['username'] = 'redhat'
            request.session['password'] = '123'
            request.session.set_expiry(10)
            return redirect('/personnel/index')
        else:
            return redirect('/personnel/login/')


def index(request):
    if request.method == 'GET':
        if request.session.get('is_login',None):
            username = request.session['username']
            password = request.session['password']
            return render(request,'home.html',{'username':username,'password':password})
        else:
            return redirect('/personnel/login')

