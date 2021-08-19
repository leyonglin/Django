from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def index(request):
    html = "<h1>这是首页</h1>"
    return HttpResponse(html)


def page_2003_view(request):
    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(html)


def pagen_view(request, pg):
    html = "<h1>这是第%s个页面</h1>" % (pg)
    return HttpResponse(html)


def op_view(request, a, op, b):
    if op == "add":
        html = "a+b=%s" % (a + b)
        return HttpResponse(html)
    elif op == "mul":
        html = "a*b=%s" % (a * b)
        return HttpResponse(html)


def cal2_view(request, x, op, y):
    if op == "sub":
        html = "%s: a-b=%s" % (op, int(x) - int(y))
        return HttpResponse(html)
    elif op == "mul":
        html = "a*b=%s" % (int(x) * int(y))
        return HttpResponse(html)


def print_request(request):
    # 在终端中打印出来,http://127.0.0.1/print_request?A=5
    print("path info is", request.path_info)
    print("method is", request.method)
    print("metadata is", request.META)
    # return HttpResponse('print request ok')
    return HttpResponseRedirect('/page/2003/')


def test_get_post(request):
    POST_FORM = '''
    <form method='post' action='/test_get_post'>
        用户名：<input type='text' name='uname'>
        <input type='submit' value='提交'>
    </form>
    '''
    if request.method == 'GET':
        # http://127.0.0.1/test_get_post?a=3&c=5
        # print(request.method)
        # print(request.GET)
        # print(request.GET['a'])
        # print(request.GET.get('c','no c'))
        # print(request.GET.getlist('a'))
        return HttpResponse(POST_FORM)
    elif request.method == 'POST':
        print('uname is', request.POST['uname'])
        return HttpResponse('post is ok')


def test_html(request):
    # 方案1
    # from django.template import loader
    # t = loader.get_template('test_html.html')
    # html=t.render()
    # return HttpResponse(html)
    # 方案1
    from django.shortcuts import render
    dic = {'username': 'linleyong', "age": 19}
    return render(request, 'test_html.html', dic)


def say_hi():
    return "hahaha"


class Dog:
    def say(self):
        return "wangwang"


def test_html_param(request):
    dic = {}
    dic['int'] = 88
    dic['str'] = "linleyong"
    dic['lst'] = ['tom', 'jack', 'lily']
    dic['dict'] = {'a': 9, "b": 8}
    dic['func'] = say_hi
    dic['class_obj'] = Dog()
    dic['h1'] = '<h1>oupt p</h1>'
    return render(request, 'test_html_param.html', dic)
    # return render(request, 'test_html_param.html', locals())


def test_if_for(request):
    # x=10
    # # locals()将局部变量组合成字典
    # return render(request, 'test_if_for.html', locals())
    dic = {}
    dic['x'] = 11
    dic['lst'] = ['tom', 'jack', 'lily', '123']
    return render(request, 'test_if_for.html', dic)


# 模板继承
def base_view(request):
    # 父模板传入变量，子模板是获取不到的
    lst = ['tom', 'jack', 'lily']
    return render(request, 'base.html', locals())


def music_view(request):
    return render(request, 'music.html')


def sport_view(request):
    return render(request, 'sport.html')


# 反向地址解析
def test_url(request):
    return render(request, 'test_url.html')


def test_url_result(request):
    return HttpResponse('test url is ok')


def test_url_result1(request, age):
    return HttpResponse('age test url is ok')


def test_url_result302(request):
    from django.urls import reverse
    url = reverse('base')
    return HttpResponseRedirect(url)


def test_static(request):
    return render(request, 'test_static.html')


def set_cookies(request):
    resp = HttpResponse('set cookies')
    resp.set_cookie('udname', 'lly', 500)
    return resp


def get_cookies(request):
    cookies = request.COOKIES.get('uuname')
    return HttpResponse('value is %s' % (cookies))


def set_session(request):
    request.session['id'] = 'lly'
    return HttpResponse('set setssion is ok')


def get_session(request):
    value = request.session['id']
    return HttpResponse('session value is %s' % (value))


# 中间件使用
def test_mw(request):
    print('i am in views')
    return HttpResponse('i am in views')


# 分页
def test_page(request):
    page_num = request.GET.get('page', 1)
    all_date = ['a', 'b', 'c', 'd', 'e']
    # 初始化paginator
    paginator = Paginator(all_date,2)
    # 初始化具体页码的page对象
    c_page = paginator.page(int(page_num))
    return render(request,'test_page.html',locals())