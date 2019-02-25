[참고자료1](http://bcho.tistory.com/821)

[참고자료2](https://www.youtube.com/watch?v=RhJIMUMJ_Do)

[html5 free](https://templated.co/caminar)

# Free html5와 Django 연동하기

1. static file url 설정해주기 
setting.py

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```

2. template file 설정해주기

원하는 template file에서 ex) index.html

```python
{% load staticfiles %}
<link rel="stylesheet" href="{% static 'wordcount/assets/css/main.css' %}"/>
```

3. url.py

    path('index/', wordcount.views.index, name="index"),
    
4.  views.py

```python
def index(request):
    return render(request,'wordcount/index.html')

def elements(request):
    return render(request,'wordcount/elements.html')
```
