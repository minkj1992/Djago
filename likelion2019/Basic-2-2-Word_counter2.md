# Home 만들기

앞서 template에 워드카운터를 만들어봅시다를 띄웠다면 이제 본격적으로 word counter를 만들어봅시다. 먼저 이런 디자인으로 html 파일을 수정해봅시다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ffdf514de-7e14-4867-907e-198e590bdc8f%2FUntitled.png)

CSS도 없고, 부트스트랩도 없는 사이트로 시작합니다. 예쁘게 꾸미는건 알아서 합시다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F56d3789c-d0ec-4f45-943f-c0ab4295bedb%2FUntitled.png)

html을 알고 있다면 이정도 쯤이야 뚝딱뚝딱! 

ABOUT을 눌러도 Count를 눌러도 아무것도 작동하지 않습니다. 이제 하나하나 기능을 만들어 봅시다.

> textarea의 name을 fulltext라고 지었습니다. 이 부분은 다음 강의에서 사용되니 기억해주세요!

# ABOUT 페이지 만들기

ABOUT을 누르면 ABOUT 페이지로 넘어가고, ABOUT페이지에서도 home으로 가기를 누르면 home으로 가도록 만들어봅시다.  

## template 만들기

wordcount의 templates폴더 안에 wordcount안에 about.html을 만듭시다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F02e64f50-1bbb-472c-9353-cd39f2620a35%2FUntitled.png)

요렇게 만들어봅시다. 

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fd24da87f-ef16-4fbc-8371-85093caa6cae%2FUntitled.png)

다시 한번 말하지만 html을 배웠다면 이정도 쯤은..

템플릿을 만들면 그다음으로 만들어야할 것은?

## view 만들기

view를 만들어야합니다. wordcount폴더안에 views.py파일을 열고 about.html을 열어주는 함수를 작성해봅시다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbbc09a2e-06cf-4e82-89d6-3a1e2a97a3f7%2FUntitled.png)

home이나 about이나 달라지는건 html 파일명 정도..

## URLconf 만들기

firstproject폴더 안에 urls.py파일을 열어 URL을 설정해줍시다. views는 이미 import 되어 있으니 path 한줄 추가해주면 됩니다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F8183025f-386f-45a4-9071-d9e5897e1a9b%2FUntitled.png)

home과 동일 논리로 만들어줍니다.

- 중간테스트

    만든 about 페이지가 잘 연결되었나 확인해봅시다. 서버를 켜고, url뒤에 /about을 적어봅시다. 브라우저에 127.0.0.1:8000/about/ 를 입력했을때 about 페이지가 뜬다면 성공

## 링크 잇기

그러면 home과 about 페이지의 링크를 이어봅시다. 먼저 홈에서 about페이지로 넘어가는 링크입니다. 

    <a href="{% url 'about' %}">ABOUT</a>

a태그 안에 위와 같이 적어줍시다.

`{% %}` 라는 이상한 녀석이 추가 되었는데 이건 django 명령어를 쓰겠다는 표현 중 하나입니다. `{% url '이름' %}`는 urls.py에서 설정했던 path를 실행시키겠다는 명령어고, 뒤에 `'이름'`은 path 설정할때 name="about"하고 적었던 부분에서 about을 의미합니다.

특정 버튼을 눌렀을때 about 페이지로 이동시키고 싶다면 `{% url 'about' %}` 이걸 주소적는 곳에 열심히 적어주시면 됩니다.

- 중간테스트

    연결되었나 확인해봅시다. 127.0.0.1:8000으로 접속해보고 ABOUT을 눌러봅시다. 페이지가 넘어간다면 성공!

똑같은 방식으로 about.html에서 home으로 넘어가는 버튼을 활성화 시켜봅시다.
