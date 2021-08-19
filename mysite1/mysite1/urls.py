"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from mysite1 import views

urlpatterns = [
    # 由上往下匹配，匹配即停止re_path
    path('admin/', admin.site.urls),
    # http://127.0.0.1/
    path('', views.index),
    # http://127.0.0.1/page/2003/  最后"/"一定要加
    path('page/2003/', views.page_2003_view),

    # re_path转换器,http://127.0.0.1/2/mul/60
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$', views.cal2_view),
    # path转换器 http://127.0.0.1/page/600
    path('page/<int:pg>', views.pagen_view),
    # http://127.0.0.1/2/mul/600
    path('<int:a>/<str:op>/<int:b>', views.op_view),
    # 打印请求内容
    path('print_request', views.print_request),
    path('test_get_post', views.test_get_post),
    # 模板
    path("test_html", views.test_html),
    path("test_html_param", views.test_html_param),
    path("test_if_for", views.test_if_for),
    # 模板继承
    path("base_html", views.base_view, name='base'),
    path("music_index", views.music_view),
    path("sport_index", views.sport_view),
    # url反向解析
    path('test/url', views.test_url),
    path('test_url_result', views.test_url_result, name='test_url_result'),
    path('test_url_result/<int:age>', views.test_url_result1, name='tr'),
    path('test/url302', views.test_url_result302, name='url302'),
    # 静态文件
    path('test_static', views.test_static),
    # cookies
    path('set_cookies', views.set_cookies),
    path('get_cookies', views.get_cookies),
    # session与cookies
    path('set_session', views.set_session),
    path('get_session', views.get_session),

    # 分布式路由 http://127.0.0.1/music/index
    path('music/', include('music.urls')),
    path('bookstore/', include('bookstore.urls')),

    # 中间件使用
    path('test_mw', views.test_mw),
    # 分页
    path('test_page', views.test_page),
]
