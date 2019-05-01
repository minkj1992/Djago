# CRUD란 무엇인가.
web에서 crud 개념
    - url을 통해서 데이터를 통제하거나 관리한다.


> 오늘 해볼것은 django 웹사이트에 crud가 구현된 크롤러 
# 디렉토리 이동
# 가상환경 키기
`souce mvenv/Scripts/activate`
# django 다운로드 받기
`pip install django`
# startproject
`django-admin startproject crud`

디렉토리 이동하기
`cd crud/`
# startapp
`python manage.py startapp movie`

# crud/settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'movie',
]
```


# crawler 생성
    - `pip install bs4 request django`


- movie 폴더 바로 밑에 parser.py를 생성해준다.

movie/parser.py
```python
# https://beomi.github.io/gb-crawling/posts/2017-03-01-HowToMakeWebCrawler-Save-with-Django.html
from bs4 import BeautifulSoup
import urllib.request
import os
from django.core.files import File
from django.conf import settings

from .models import Movie



def parse_movie():
    movies = []
    ##### 크롤링 시작
    url = urllib.request.urlopen("https://movie.naver.com/movie/running/current.nhn")
    bs = BeautifulSoup(url, 'html.parser')
    body = bs.body
    target = body.find(class_="lst_detail_t1")
    list = target.find_all('li')
    no = 1
    iteration = min(100,len(list))
    for n in range(0, iteration) :
        movie = {}
        no += 1
        # 영화 제목
        title = list[n].find(class_="tit").find("a").text.strip()
        movie['title']=title
        score = list[n].find(class_="star").find(class_="star_t1").find("a").find(class_='num').text.strip()
        movie['score']=score 
        

        # https://vinta.ws/code/read-and-save-file-in-django-python.html 이거만 보면 된다.
        # 포스터
        try:
            img_url = list[n].find(class_="thumb").find("a").find("img").get("src")
            # file_name = title+'.jpg'
            # img = Image.open(StringIO(img_url.content))
            # img_io = StringIO()
            # img.save(img_io, 'JPG', quality=100)
            # file_dir = settings.MEDIA_ROOT + file_name
            # resp = urllib.request.urlretrieve(img_url,file_dir)
            # Movie.image.save(file_name, ContentFile(img_io.getvalue()), save=False)
            # 참고 https://docs.djangoproject.com/en/2.2/ref/files/file/
            # Movie.image.save(file_name, img_url.content, save=False)
            # Movie.image.save(file_name, ContentFile(img_url.content), save=False)
            # with open(file_dir, 'rb') as f:
            #     Movie.image = File(f)
            
            
            movie['img_url'] = img_url
        except:
            pass

        
        # 개봉일/ 장르/ runtime
        try:
            # ['액션, SF', '181분', '2019.04.24 개봉']
            value = list[n].find(class_="info_txt1").find_all("dd")[0].text.replace("\n",'').replace("\t", "").replace('\r','').split('|')
            genre = [i.strip() for i in value[0].split(',')]
            movie['genre']=','.join(genre)
            length = int(value[1][:-1])
            movie['length']=length
            date = value[2].split()[0]
            movie['date']=date
        except IndexError:
            movie['genre']="데이터없음"
            movie['length']="데이터없음"
            movie['date']="데이터없음"
        # 감독
        try:
            director = list[n].find(class_="info_txt1").find_all("dd")[1].find("span").find_all("a")
            directorList = [director.text.strip() for director in director]
            movie['director']=','.join(directorList)
        except IndexError:
            movie['director']="데이터없음"
        # 출연 배우
        try:
            cast = list[n].find(class_="lst_dsc").find("dl", class_="info_txt1").find_all("dd")[2].find(class_="link_txt").find_all("a")
            castList = [cast.text.strip() for cast in cast]
            movie['actors']=','.join(castList)
        except IndexError:
            movie['actors'] = "데이터없음"
        
        
        movies.append(movie)
    
    for m in movies:
        Movie(title=m['title'],
        score=m['score'],
        genre=m['genre'],
        date = m['date'],
        length=m['length'],
        director=m['director'],
        actors = m['actors'],
        img_url = m['img_url'],
        ).save()


```

# 네이버 영화 데이터 꼴 생성
movie/models.py

```python
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    director= models.CharField(max_length=1000)
    actors= models.CharField(max_length=1000)
    date= models.CharField(max_length=1000)
    length= models.IntegerField()
    score = models.FloatField()
    genre = models.CharField(max_length=1000)
    img_url = models.CharField(max_length=1000)

```

# url 설정

settings.py가 있는폴더/urls.py
```python
from django.contrib import admin
from django.urls import path
import movie.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',movie.views.MovieList.as_view(),name="home"),
    path('parse',movie.views.parse,name="parse"),
    # 아래 부터 CRUD 4가지 
    # 영화를 생성할 url (Create)
    path('create/',movie.views.MovieCreate.as_view(),name="create"),
    # 각 영화 detail url(Read)
    path('detail/<int:pk>',movie.views.MovieDetail.as_view(),name="detail"),
    # 영화를 수정할 url (Update)
    path('update/<int:pk>',movie.views.MovieUpdate.as_view(),name="update"),
    # 영화를 제거할 url (Delete)
    path('delete/<int:pk>',movie.views.MovieDelete.as_view(),name="delete"),
]

```

- 중요한점은 `CBV`를 활용하기 위해서는 `.as_view()`를 url 뒤에 붙여주어야 한다.

- `'delete/<int:pk>'`와 같이 url 뒤에 primary_key(영화가 데이터베이스에 저장된 id)를 전달해주는데, 이렇게 하는 이유는 어떤 특정환 영화 게시물을 수정/삭제/상세보기 할 것인지 명확하게 하기 위해서 이다.


# `CBV(Class Based View)`
장고에서 View(`views.py`)는 
- `FBV(Function Based View)`
    - 지금까지 우리가 했던 `def home()`와 같은 함수를 만들어서 관리해주는 방법
    - 우리 입맛대로 수정하기가 편한다.
- `CBV(Class Based View)`
    - django에서 편의를 위하여 제공해주는 방법, 장고에서 미리 `class`를 정의 내려주고, 우리는 해당 `class`를 `상속`받아서 편하게 기능 구현 할 수 있다. 
    - `장점`: 장고에서 제공해주는 기능은 빠르게 생성할 수 있다. 특히 `ListView`의 경우에는 `CRUD`또한 제공해준다.
    - `단점`: 미리 틀을 제공해주어 우리 입맛대로 수정하기가 어려울 때가 있다.

이렇게 두가지 방법을 통하여 작성될 수 있다.

오늘은 이 `CBV`방식으로 편하게 `CRUD`기능 구현을 해보도록 하겠습니다.

# `django ListView(CBV)`
> 여러 목록들을 보여주고 싶을때, 예를 들면 게시판을 만들고 게시판 글들 목록과 함께 CRUD를 제공하고 싶을 경우 **`ListView`** 와 아이들 클래스를 활용하면 편합니다.


장고의 `ListView`를 통하여 손쉽게 영화 목록들을 보여주도록 하자.

- `ListView`: list의 목록을 가져올 수 있다.
- `CreateView`: list의 항목을 추가할 수 있다.(`C`)
- `DetailView`: list의 항목의 detail을 보여줄 수 있다.(`R`)
- `UpdateView`: list의 항목을 수정할 수 있다.(`U`)
- `DeleteView`: list의 항목을 제거할 수 있다.(`D`)


movie/views.py
```python
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Movie
from django.urls import reverse_lazy
from .parser import parse_movie

def parse(request):
    parse_movie()
    return redirect('home')

class MovieList(ListView):
    model = Movie
    template_name = 'home.html'
class MovieCreate(CreateView):
    model = Movie
    fields =  '__all__'
    template_name = 'movie_form.html'
    success_url = reverse_lazy('home')
class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
class MovieUpdate(UpdateView):
    model = Movie
    fields =  '__all__'
    template_name = 'movie_form.html'
    success_url = reverse_lazy('home')
class MovieDelete(DeleteView):
    model = Movie
    template_name = 'movie_delete.html'
    success_url = reverse_lazy('home')

```

- `model` = 어떤 데이터베이스(model)을 연결해줄지 명시
- `template_name` = 연결해줄 `html`파일 이름 명시
- `success_url` = CRUD 중 어떤한 업무를 완수했을 경우, 어디 url로 이동할지(redirect) 명시해주는 부분
- `reverse_lazy`는 `reverse`와 같은 기능인데 `generic view`에서 주로 사용한다. 
타이밍 로딩 문제로 `generic view`에서는 `reverse`는 사용할 수 없고 `reverse_lazy`를 사용해야한다.

# 템플릿(Templates)

> 모든 crud를 완성했고 이제 보여주는 html만 생성해주면 된다.

- `movie/templates`: movie 폴더 바로 밑에 `templates`를 생성해준다.
- 이후 5가지 `html`파일을 만들어준다.
    - `home.html`: 시작 페이지,영화 목록 보여줄 페이지
    - `movie_form.html`: 영화 새로 생성페이지, 영화 수정 페이지 (`C`,`U`)
    - `movie_detail.html`: 영화 상세 페이지(`R`)
    - `movie_delete.html`: 영화 삭제페이지, 엄밀하게는 삭제 시 확인 메시지를 보여주는 페이지(`D`)


movie/templates/home.html
```html
<h1>Home</h1>

<table border="1">
<thead>
    <tr>
    <th>포스터</th>
    <th>영화제목</th>
    <th>감독</th>
    <th>배우</th>
    <th>출시일</th>
    <th>상영시간</th>
    <th>평점</th>
    <th>영화장르</th>
    <th>상세보기</th>
    <th>수정하기</th>
    <th>삭제하기</th>
    </tr>
</thead>
<tbody>
{% for movie in object_list %}
    <tr>
    <td><img src='{{ movie.img_url }}'></td>
    <td>{{ movie.title }}</td>
    <td>{{ movie.director }}</td>
    <td>{{ movie.actors }}</td>
    <td>{{ movie.date }}일</td>
    <td>{{ movie.length }}분</td>
    <td>{{ movie.score }}/10점</td>
    <td>{{ movie.genre }}</td>
    <td><a href="{% url 'detail' movie.id %}">detail</a></td>
    <td><a href="{% url 'update' movie.id %}">update</a></td>
    <td><a href="{% url 'delete' movie.id %}">delete</a></td>
    </tr>
{% endfor %}
</tbody>
</table>

<a href="{% url 'create' %}">new</a>
<a href="{% url 'parse' %}">크롤링시작</a>
```
movie/templates/movie_detail.html
```html
<h1>detail</h1>

{{ object.title }}<br/>
{{ object.director }}<br/>
{{ object.actors }}<br/>
{{ object.date }}<br/>
{{ object.length }}<br/>
{{ object.score }}<br/>
{{ object.genre }}<br/>
<img src ="{{ object.img_url }}"/><br/>

<a href="{% url 'home' %}" >home</a>
```

movie/templates/movie_delete.html
```html
<h1>delete</h1>
<form method="post">{% csrf_token %}
    Are you sure you want to delte {{ object.title }}? 
    <input type="submit" value="submit"/>
</form>
```




# 마지막으로 
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`


