from django.http import HttpResponse
import json
from rest_framework.views import APIView
from . import models
from rest_framework import serializers

# class ParamVersion(object):
#     def determine_version(self, request, *args, **kwargs):
#         version = request.query_params.get('version')
#         return version


class UsersView(APIView):
    # versioning_class = URLPathVersioning

    def get(self, request, *args, **kwargs):
        print(request.version)
        return HttpResponse('版本为: '+request.version)

class ParserView(APIView):

    # parser_classes = [JSONParser, FormParser]

    def post(self, request, *args, **kwargs):
        print(request.data)
        return HttpResponse('ParserView')




class RolesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

class RolesView(APIView):

    def get(self, request, *args, **kwargs):
        # roles = models.Role.objects.all().values('id', 'title')
        # print(type(roles))
        # roles = list(roles)
        # ret = json.dumps(roles, ensure_ascii=False)

        roles = models.Role.objects.all()
        ser = RolesSerializer(instance=roles, many=True)
        ret = json.dumps(ser.data, ensure_ascii=False)

        return HttpResponse(ret)



# class UserInfoSerializer(serializers.Serializer):
#
#     用户类型 = serializers.IntegerField(source="user_type")
#     utp = serializers.CharField(source="get_user_type_display")
#     username = serializers.CharField()
#     password = serializers.CharField()
#     gp = serializers.CharField(source="group.title")
#     # rls = serializers.CharField(source="roles.all")
#
#     rls = serializers.SerializerMethodField() # 自定义显示
#
#     def get_rls(self, row):
#
#         role_obj_list = row.roles.all()
#
#         ret = []
#         for item in role_obj_list:
#             ret.append({'id': item.id, 'title': item.title})
#         return ret


class UserInfoSerializer(serializers.ModelSerializer):

    # 用户类型 = serializers.CharField(source="get_user_type_display")
    # rls = serializers.SerializerMethodField()
    # def get_rls(self, row):
    #
    #     role_obj_list = row.roles.all()
    #     ret = []
    #     for item in role_obj_list:
    #         ret.append({'id': item.id, 'title': item.title})
    #
    #     return ret

    class Meta:
        model = models.Userinfo

        fields = "__all__"
        depth = 1
        # fields
        #
        # = ['id', 'username', 'password', '用户类型', 'rls']

class UserInfoView(APIView):

    def get(self, request, *args, **kwargs):

        users = models.Userinfo.objects.all()
        ser = UserInfoSerializer(instance=users, many=True)
        ret = json.dumps(ser.data, ensure_ascii=False)

        return HttpResponse(ret)