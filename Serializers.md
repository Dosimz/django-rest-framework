## Serializers

- #### 直接继承 `serializers.Serializer`

  ```python
  	＃ 实现序列化类
  class RolesSerializer(serializers.Serializer):
      id = serializers.IntegerField()
      title = serializers.CharField()
  ```
```
  
>  指定序列化字段
  

  

  
  ```python
  class RolesView(APIView):
  
      def get(self, request, *args, **kwargs):
      	# 不继承 serializers
          # roles = models.Role.objects.all().values('id', 'title')
          # print(type(roles))
          # roles = list(roles)
          # ret = json.dumps(roles, ensure_ascii=False)
  		
  		# 从数据库拿到数据
          roles = models.Role.objects.all()
          # 使用 Serializer 类解析
          ser = RolesSerializer(instance=roles, many=True)
          # ensure_ascii = False 使中文字符串可以显示
          ret = json.dumps(ser.data, ensure_ascii=False)
  
          return HttpResponse(ret)
```

  


- ####  使用 `serializers.SerializerMethodField()`

  > 指定序列化字段

  ```python
  class UserInfoSerializer(serializers.Serializer):
  	# source= 参数为 models.py 中的字段
      用户类型 = serializers.IntegerField(source="user_type")
      # 如果传方法进去，会自动在源码执行 `fun()`．
      utp = serializers.CharField(source="get_user_type_display")
      # 不使用 source 时，变量名要和字段对应
      username = serializers.CharField()
      password = serializers.CharField()
      gp = serializers.CharField(source="group.title")
      
  ```

  > 使用 `serializers.SerializerMethodField()` 自定义字段．

  ```python
   	# 上接　UserInfoSerializer　类
      rls = serializers.SerializerMethodField() # 自定义显示
  		# 这里方法名要使用 get_ +　rls (前面的变量名)
      	def get_rls(self, row):
  			# row 是当前行
          	role_obj_list = row.roles.all()
  
          	ret = []
              
          	for item in role_obj_list:
              	ret.append({'id': item.id, 'title': item.title})
          	return ret
  ```

  



- ####  继承 `ModelSerializer` 类

  与直接继承 `serializers.Serializer` 不同，继承 `ModelSerializer` 后，可以使用一个超能力．

  ```python
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
          # fields = ['id', 'username', 'password', '用户类型', 'rls']
  
  ```
  
  

Meta 类会显示 `models.Userinfo` 中的所有字段．
可以使用　`fields = ['id',......]` 来限定序列化的内容，也可以在其中加入自定义的属性．

-------






> 默认的 `fields = "__all__"` 序列化的内容，有的只有 id 号．




![](/run/media/yuyi/068AE93F8AE92BBD/python/django-rest-framework/img/Serializer_00.png)



----------------





> 可以加入 `depth = 1` 来序列化更深层的内容．`depth` 的参数最好限定在(1-4)．






![](/run/media/yuyi/068AE93F8AE92BBD/python/django-rest-framework/img/Serializer_01.png)