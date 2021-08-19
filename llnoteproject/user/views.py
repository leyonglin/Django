import hashlib

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from user.models import User


def reg_view(request):
    if request.method == 'GET':
        return render(request,'user/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        if password_1 != password_2:
            return HttpResponse('两次密码输入不同')
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('用户已注册')

        # 实例化对象
        m = hashlib.md5()
        # 传入byte数据
        m.update(password_1.encode())
        password_m = m.hexdigest()
        try:
            user = User.objects.create(username=username,password = password_m)
        except Exception as e:
            print('---create user error %s'%(e))
            return HttpResponse('用户已注册')

        # 免登录一天
        request.session['username']=username
        # 主键比其它索引查询效率高
        request.session['uid'] = user.id

        return HttpResponse('注册成功')

def login_view(request):
    if request.method == 'GET':
        # 检查session
        if request.session.get('username') and request.session.get('uid'):
            return HttpResponseRedirect('index/index.html')
        # 检查cookies
        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            return HttpResponseRedirect('index/index.html')
        return render(request,'user/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            print(user)
        except Exception as e:
            print('--- login error %s'%(e))
            return HttpResponse('用户名或密码错误')

        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('密码或用户名错误')
        
        #记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id
        # return HttpResponse('登录成功')

        # 判断用户是否点选了'记住用户名' , 可以打开浏览器调试，查看post提交了什么数据
        # 点选了 --> cookies 存储 username,uid 时间3天
        resp = HttpResponse('登录成功')
        if 'remember' in request.POST:
            resp.set_cookie('username',username,3600*24*3)
            resp.set_cookie('uid',user.id,3600*24*3)
        return resp
