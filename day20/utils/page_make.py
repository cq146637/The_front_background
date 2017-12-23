from django.utils.safestring import mark_safe

class Page:
    def __init__(self,request_page,all_count,path_info,every_page_count=10,every_page_num=7):
        self.request_page = request_page            #用户请求页号
        self.all_count = all_count                  #展示列表总长度
        self.path_info = path_info                  #请求页面URL
        self.every_page_count = every_page_count    #默认每页显示的列表长度
        self.every_page_num = every_page_num        #默认一页有几个跳转页
        self.page_list = []
    def start(self):
        #返回展示列表的首索引
        return (self.request_page-1)* self.every_page_count
    def end(self):
        # 返回展示列表的尾索引
        return self.request_page * self.every_page_count
    def total_count(self):
        #返回列表分页显示后的总页数，长度为100的列表，每夜显示10行，可以分的页数总共为10页
        count, y = divmod(self.all_count,self.every_page_count)
        if y:
            count += 1
        return count

    def index(self):
        #返回当前请求页号在列表中的索引值范围
        start_index = self.request_page - self.every_page_num // 2
        end_index = self.request_page + self.every_page_num // 2 +1
        count = self.total_count()
        if count < self.every_page_num:
            start_index = 1
            end_index = count + 1
        else:
            if self.request_page <= (self.every_page_num // 2 + 1):
                start_index = 1
                end_index = self.every_page_num + 1
            elif (self.request_page + self.every_page_num // 2) > count:
                start_index = count - self.every_page_num + 1
                end_index = count + 1
        return start_index,end_index


    def page_str(self):
        #返回生成的HTML标签
        start_index, end_index = self.index()
        count = self.total_count()
        first_page = "<a href='%s?pid=1'>首页</a>"%self.path_info
        self.page_list.append(first_page)
        if self.request_page == 1:
            prev_page = "<a href='javascript:void(0);'>上一页</a>"
        else:
            prev_page = "<a href='%s?pid=%s'>上一页</a>" % (self.path_info,self.request_page - 1)
        self.page_list.append(prev_page)
        for i in range(start_index, end_index):
            if i == self.request_page:
                temp = "<a class='active' href='%s?pid=%s'>%s</a>" % (self.path_info,i, i)
            else:
                temp = "<a href='%s?pid=%s'>%s</a>" % (self.path_info,i, i)
            self.page_list.append(temp)
        if self.request_page == count:
            next_page = "<a href='javascript:void(0);'>下一页</a>"
        else:
            next_page = "<a href='%s?pid=%s'>下一页</a>" % (self.path_info,self.request_page + 1)
        self.page_list.append(next_page)
        last_page = "<a href='%s?pid=%s'>尾页</a>" % (self.path_info,count)
        self.page_list.append(last_page)
        jump_page = """
            <input id='jump_page' type='text' /><a onclick='jumpPage(this,"%s?pid=");'>跳转</a>
            <script>
                function jumpPage(ths,url){
                    var val = parseInt(ths.previousSibling.value);
                    if( val>0 && val<%s+1){
                        location.href = url + ths.previousSibling.value;
                    }
                    else{
                        ths.previousSibling.value = '';
                        return false;
                    }
                }
            </script>
            """ % (self.path_info,count)
        self.page_list.append(jump_page)
        page_str = "".join(self.page_list)
        page_str = mark_safe(page_str)
        return page_str