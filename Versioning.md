## Versioning 

API 版本控制可以使你同时拥有多个版本。

## Versioning with REST framework

REST framework 提供了一些不错的版本控制方案。

- ### QueryParameterVersioning
    `QueryParameterVersioning` 类已经把版本检测等函数写好了．
    因此,我们只需要配置一些参数,即可使用.
    
    
    
     ##### setting.py 配置文件中配置.

		```python3
		REST_FRAMEWORK = {
		# 配置板块控制要使用的类
		"DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.QueryParameterVersioning"
		
		# 默认版本
		"DEFAULT_VERSION": "v1",
		# 可以使用的版本
		"ALLOWED_VERSIONs": ["v1, v2"],
		 # 版本号对应的关键字
		 "VERSION_PARAM": "version"
		 }
		```

![](/run/media/yuyi/068AE93F8AE92BBD/python/django-rest-framework/img/versioning_00.png)


- ### URLPathVersioning
    与 `QueryParameterVersioning` 从 get 方法的参数中检测版本不同,`URLPathVersioning` 是从 url 中检测版本.
    
    
    
     ##### setting.py 配置文件中配置.

		```python3
		REST_FRAMEWORK = {
		"DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning"
		 }
		```
		> 需要注意的是,使用 `URLPathVersioning` 类,要在 urls.py 文件中配置正则表达式辅助检测版本.
	
	

	```python3
    # api/urls.py
    urlpatterns = [
        url(r'^(?P<version>[v1|v2]+)/users/,views.UsersView.as_view()),
    ]
    ```



> 这里直接从 url 来获取版本 

![](/run/media/yuyi/068AE93F8AE92BBD/python/django-rest-framework/img/versioning_01.png)

## Custom versioning schemes

```python3
# views.py
class ParamVersion(object):
    def determine_version(self, request, *args, **kwargs):
        version = request.query_params.get('version')
        return version
        
class UsersView(APIView):
	# 声明要使用的类
    versioning_class = ParamVersion

    def get(self, request, *args, **kwargs):
        print(request.version)
        return HttpResponse('版本为: '+request.version)
```