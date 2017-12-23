from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class Middle1(MiddlewareMixin):
    def process_request(self,request):
        print('第一个中间件的请求函数')

    def process_view(self,request, callback_func, callback_func_args, callback_func_kwargs):
        print('第一个中间件的视图函数')

    def process_exception(self, request, exception):
        #如果views函数中执行出错，自动执行
        if isinstance(exception, ValueError):
            print('第一个中间件的异常处理函数')

    def process_response(self,request,response):
        print('第一个中间件的回复函数')
        return response

    def process_template_response(self, request, response):
        #默认不执行
        #如果views返回的对象中具有render方法，该方法自动执行
        print('第一个中间件的模板函数')
        return response

class Middle2(MiddlewareMixin):
    def process_request(self,request):
        print('第二个中间件的请求函数')

    def process_view(self,request, callback_func, callback_func_args, callback_func_kwargs):
        print('第二个中间件的视图函数')

    def process_exception(self, request, exception):
        #如果views函数中执行出错，自动执行
        if isinstance(exception, ValueError):
            print('第二个中间件的异常处理函数')
            # return HttpResponse("发生ValueError错误。。。")

    def process_response(self,request,response):
        print('第二个中间件的回复函数')
        return response
    def process_template_response(self, request, response):
        #默认不执行
        #如果views返回的对象中具有render方法，该方法自动执行
        print('第二个中间件的模板函数')
        return response

class Middle3(MiddlewareMixin):
    def process_request(self,request):
        print('第三个中间件的请求函数')

    def process_view(self,request, callback_func, callback_func_args, callback_func_kwargs):
        #url(r'^user_list\d+', views.user_list)
        #callback_func_args   --> 存没有变量名的参数
        #url(r'^user_list(?P<nid>\d+)', views.user_list)
        #callback_func_kwargs --> 存有变量名的参数
        print('第三个中间件的视图函数')

    def process_response(self,request,response):
        print('第三个中间件的回复函数')
        return response

    def process_exception(self, request, exception):
        #如果views函数中执行出错，自动执行
        if isinstance(exception,ValueError):
            print('第三个中间件的异常处理函数')
            #return HttpResponse("发生ValueError错误。。。")

    def process_template_response(self, request, response):
        #默认不执行
        #如果views返回的对象中具有render方法，该方法自动执行
        print('第三个中间件的模板函数')
        return response