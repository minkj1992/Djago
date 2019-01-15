이제 본격적으로 첫번째 프로젝트를 시작해봅시다. Word Counter라는 사이트를 만들겁니다.

문자열을 받아, 각 단어가 몇번 나왔는지 단어별로 세주는 사이트라고 생각하면 됩니다. (기능은 거기에 한참 못미칠테지만.. 기능이 아니라 django에 집중을 해봅시다.)


project → app → app등록 → template 만들기 → view 만들기 → url연결 

이 순서를 따라가며 하나하나 자세히 알아봅시다.

# Django 프로젝트 시작하기

프로젝트 시작전 잊지 말아야 할 것이 있습니다. 가상 환경을 만들고 가상환경을 켜둔 상태에서 진행해야합니다. django가 깔리지 않았다면 `pip install` 을 통해 설치도 해줍니다. 어떻게 해야하는지 생각이 안난다면 이전 내용을 복습하고 오세요.

## project 시작하기

    django-admin startproject firstproject

위 명령어를 통해 `firstproject`를 생성합니다.

> 꼭 가상환경이 활성화 된 상태에서 작업해주세요.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fa9cfe4a4-0236-461c-94ce-d04f84cd3c87%2FUntitled.png)

만들면 firstproject 가 생기고 그 안에 firstproject 폴더가 있습니다. 공부할때 헷갈리니까 상위 폴더 이름 'first_assignment'을 바꿔주세요.

만들면 firstproject 가 생기고 그 안에 firstproject 폴더가 있습니다. 공부할때 헷갈리니까 상위 폴더 이름 'first_assignment'을 바꿔주세요.

프로젝트를 만들었으니 app을 만들 차례입니다. 학습의 편의를 위해 터미널 경로가 manage.py가 있는 폴더 안에 있게 합시다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbe2bc222-8d32-4aff-b85d-0b8a591ef3fc%2FUntitled.png)

터미널 경로가 위와 같이 설정되었으면 완성!

## app 만들기

생각이 나지 않는다면 cheat sheet를 활용하면 됩니다. 그러라고 만들어 둔거니 부담없이 활용하세요.

    python manage.py startapp wordcount

wordcount라는 앱을 만들겠다는 명령어 입니다. 앞서 설명했듯, 장고 프로젝트는 여러 개의 앱으로 구성됩니다. 지금은 이해하지 못해도 괜찮습니다. (앱을 한번 만들때 잘만들어두면 다른 사이트 만들때 그 앱을 그대로 가져다가 쓸수도 있습니다.)

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F35d5f30b-d49e-45af-b3a9-6585855230d9%2FUntitled.png)

터미널에 다른 앱을 만드는 명령어 이외의 명령어는 django 설치와 pip 버전 업그레이드 관련 부분이니 진행과정중 에러가 발생하지 않는다면 신경쓰지 않으셔도 됩니다.

이제 왼쪽의 폴더창을 보면 wordcount라는 폴더가 추가되었습니다.

앱을 만들었으니 settings.py로 가서 app을 쓰겠다고 알려줘야합니다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F72a3761b-2f40-4ed1-9fc7-1c28cf54dcb5%2FUntitled.png)

'wordcount.apps.WordcountConfig' 다음에 `,` 를 꼭 찍어줘야합니다!

`INSTALLED_APPS`에 wordcount.apps.WordcountConfig 를 추가해줍니다. 다시한번 설명하자면, wordcount폴더안에 apps란 파일에 WordcountConfig로 되어있는 클래스를 등록해주는 절차입니다. ('왜해요?' 라고 물어보신다면,  검색해보라 답해드리겠습니다.)

## template 만들기

이제 app에서 home이 될 페이지를 만들어봅시다. 먼저 wordcount폴더안에 templates라는 폴더를 만듭시다. 그 아래 다시 wordcount라는 폴더를 만듭시다. 그리고 그 안에 home.html 파일을 만들고 아래와 같이 내용을 채워봅시다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F21447d7f-1b01-4e41-8772-fc556d8edb85%2FUntitled.png)

## View 만들기

보여줄 화면을 만들었으니 이제 연결을 해야겠죠. wordcount폴더 안에 views.py파일을 엽니다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F0cf56ef0-0fea-431c-b122-a02fcf3c326e%2FUntitled.png)

render(request, 'wordcount/home.html') 여기서 request 뒤에 적는 내용은 home.html이라는 template이 위치하는 경로입니다.

앞서 템플릿을 templates/wordcount/home.html 경로에 만들었기 때문에 wordcount/home.html로 적어줍니다.  

## URLconf 연결

이제 URL을 연결해봅시다. urls.py파일을 열어봅시다. views.py파일 안에 만들어 놓은 home함수를 이용하기 위해서는 urls.py에 views.py을 `import`해야합니다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F09183ac7-84d9-44ef-8488-c4c7f30f9999%2FUntitled.png)

안에 입력하는 내용은 조금 기계적으로 생각해도 괜찮습니다.

18번째 줄과, 22번째 줄의 내용이 추가된 내용입니다.

각 줄의 의미는 다음과 같습니다.

18번째줄 : wordcount라는 폴더안에 views파일을 `import`해라.

22번째줄 : ''로 url요청이 들어오면 wordcount폴더안에 views라는 파일안에 있는 home이라는 함수를 실행한다. 이런 `path`를 home이라고 부른다.

## 서버를 켜봅시다.

    python manage.py runserver

manage.py파일이 있는 경로에서 실행해야합니다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F6139317a-631a-4cf6-b043-ab8cc3e8138c%2FUntitled.png)

이리 나오면 잘만든 겁니다. 앞선 hello world 예제와 크게 다른 점이 없기에 잘 따라왔을거라 믿습니다.
