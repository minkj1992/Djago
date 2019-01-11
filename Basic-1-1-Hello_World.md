# Django로 프로젝트 시작하기

## 가상환경 켜기

장고 프로젝트를 시작하려면 가장 먼저 가상환경을 켜야합니다.

    source myvenv/Script/Activate
    
## 첫번째 Django 프로젝트 시작하기

가상환경이 켜진 상태에서 바로 아래 명령어를 입력해서 프로젝트를 만듭니다.

    django-admin startproject firstsite

`startproject` 뒤에는 만들고 싶은 파일명을 적으면 되지만 지금은 그냥 `firstsite`로 통일합니다.


Terminal상에서 파일명을 rename하고 싶을 경우에는 mv "old" "new"

firstsite 안에 firstsite라는 폴더가 생겼습니다. 지칭이 헷갈릴것 같으니 상위 폴더 이름을 firstsiteproject로 바꿔줍니다. 
그리고 그 폴더 안으로 터미널 경로를 이동 합시다.

    (myvenv) minwookje@minwookje-900X5L:~/code/python/django$ mv ./firstsite/ ./firstProject


열어보면 원가 많은 파일들이 생겼습니다. 간단한 설명은 아래 해두었으니 참고하세요.

- `startproject`로 생성된 파일들
    - manage.py : django 프로젝트와 다양한 방법으로 상호작용 하는 파일입니다. 열어볼 필요 없습니다. 그냥 중요한 친구구나 정도 생각해주세요.
    - __ init __.py : '이 친구도 잘모르겠으니 건드리지 말아야지.' 라고 생각하셨다면 잘하신겁니다.
    - settings.py : django 프로젝트의 환경/구성을 저장하는 파일입니다. 종종 열어서 수정을 해줘야합니다.
    - urls.py : Django 프로젝트의 URL 들을 관리합니다. 자주쓰고 이 친해져야 하는 파일입니다.
    - wsgi.py : 지금은 몰라도 됩니다.

## Django 서버 작동시키기

    python manage.py runserver

 http://127.0.0.1:8000/ 로 브라우저 창을 열어봅시다.
 
 서버를 끄려면 서버가 실행중인 터미널창에서 `ctrl` + `c`를 누르면 됩니다.
 
 
# Hello World 페이지 띄워보기

> 지금 까지 서버를 실행 하였다면, 내가 만든 페이지를 웹에 띄우는 작업을 하려 한다. 그러기 위해서는 `app`을 만들어야 한다.

## app 만들기

- `app`: 프로젝트의 구성 단위

app을 만들때 어디에 만들어도 상관은 없지만, 편의를 위해 manage.py 있는 폴더에서 명령을 내리는 것을 추천

    python manage.py startapp hello
    
![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Faeecbf3b-f135-4991-825d-17a027c2f224%2FUntitled.png?width=1840)

뭐가 이렇게 많아...

hello 폴더 안에서 일단 알아야 할 파일은 views.py 입니다. 앞으로 페이지 만들기 위해서는 아래순서에 따라 작업해야한다고 외워둡시다.

1. settings.py ⇒ project에게 app의 존재 알리기
2. templates ⇒ views.py에서 처리된 데이터를 받아 사용자에게 화면을 보여줌
3. views.py ⇒ 데이터를 처리하는 함수 작성
4. urls.py ⇒ 요청에 맞는 함수를 views.py에서 찾아 요청 전달

**settings.py** → **templates**  → **views.py → urls.py** 순으로 연결하는 작업을 하면됩니다. 작업순서는 그냥 외우면 좋습니다.

(개발에 정해진 작업순서는 없지만, 학습의 편의를 위해 정한 순서입니다. 실제 개발은 왔다갔다하며 이루어집니다.)

