from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView

from . import models
from .utils import auth, permission, throttling


# Create your views here.

def md5(user):
    import hashlib
    import time

    ctime = str(time.time())

    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()

class AuthView(APIView):
    '''用于用户登录认证'''

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            obj = models.UserInfo.objects.filter(username=user, password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'
            token = md5(user)
            models.UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            ret['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'
        print(request.user)
        return JsonResponse(ret)


class AccountView(APIView):
    '''用于展示用户界面'''

    authentication_classes = [auth.Authtication, ]
    throttle_classes = [throttling.VisitThrottle, ]

    def get(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None, 'data': None}
        try:
            ret['data'] = '个人账户信息'
        except Exception as e:
            pass
        # print(request.user)
        return JsonResponse(ret)

class VIPinfo(APIView):

    authentication_classes = [auth.Authtication, ]
    permission_classes = [permission.Mypermission, ]

    def get(self, request, *args, **kwargs):
        return HttpResponse('欢迎您，我们尊贵的超级会员专属VIP特权用户！')