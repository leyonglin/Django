from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re

class MyMW1(MiddlewareMixin):
    # 进入路由urls前, 返回None则表示通过
    def process_request(self, request):
        print('1pre urls')

    # 进入视图views前, 返回None则表示通过，callback表示视图函数，callback_args,callback_kwargs表示视图函数参数
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('1pre views')

    # response返回客户端前
    def process_response(self, request, response):
        print('1pre response')
        return response


class MyMW2(MiddlewareMixin):
    # 进入路由urls前, 返回None则表示通过
    def process_request(self, request):
        print('2pre urls')

    # 进入视图views前, 返回None则表示通过，callback表示视图函数，callback_args,callback_kwargs表示视图函数参数
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('2pre views')

    # response返回客户端前
    def process_response(self, request, response):
        print('2pre response')
        return response

# 访问限制
class VisiteLimit(MiddlewareMixin):

    # 次数统计正常应该存储在内存数据库中，这里直接设置为类属性，重启django则会清空
    visit_times={}

    def process_request(self,request):
        ip_address = request.META['REMOTE_ADDR']
        path_url= request.path_info
        if not re.match('/test_mw',path_url):
            # 返回Null则代表放行
            return
        times = self.visit_times.get(ip_address,0)
        print('ip',ip_address,'已经访问',times)
        self.visit_times[ip_address] = times+1
        if times < 5:
            return
        return HttpResponse('你已经访问过'+str(times)+'次')

