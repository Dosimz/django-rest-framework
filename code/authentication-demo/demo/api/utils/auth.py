from rest_framework.authentication import BaseAuthentication
from .. import models
from rest_framework import exceptions

class Authtication(BaseAuthentication):

    def authenticate(self, request):
        token = request._request.GET.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return (token_obj.user, token_obj)