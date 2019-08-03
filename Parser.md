## Parsers

选择和请求头 content-type 中对应的解析器,对请求体内容进行解析





## Setting the parsers

- 全局设置解析器

```python3
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}
```

>  这里使用了 REST framework 内置的 JSONParser 类.将指定只解析带有 JSON 格式请求体的请求

- 局部设定解析器

```python3
class ParserView(APIView):
	parser_classes = [JSONParser, ]
	
	def post(self, request, *args, **kwargs):
		print(request.data)
		return HttpResponse('ParserView')
```

