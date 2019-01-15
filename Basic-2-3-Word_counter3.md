이제 첫번째 과제에서 가장 어렵고 핵심인 부분인 count 기능을 구현해야합니다. 

# count 페이지 만들기

앞서 다른 페이지를 만들었던 것과 똑같은 방식으로 count 페이지를 만들어 봅시다. 입력받은 데이터를 표시해야될 부분을 주석으로 표시했습니다. 다음 html 파일을 보고 만들어질 화면을 상상해보세요.

    <h1>당신이 입력한 텍스트는 <!--총단어수--> 단어로 구성되어 있습니다.</h1>
    
    <a href="{% url 'home' %}"> 다시하기 </a>
    
    <h1>입력한 텍스트: </h1>
    <!-- 입력받은 전체 텍스트 -->
    
    <h1>단어 카운트:</h1>
    <!-- '단어' - '단어나온 횟수' -->

다시하기를 누르면 home으로 넘어갈수 있는 링크를 추가했습니다. (이제 이정도는 알아서 하십쇼)

# home 에서 데이터 받아 count페이지로 넘겨주기

home에서 만든 textarea에서 submit 버튼을 누르면 입력받은 데이터가 가공되어 count페이지로 넘어가야합니다.

view부터 작성해봅시다.

## view 만들기

일단 배운걸 활용해 view와 url을 작성해봅시다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fb72fe784-ef67-4807-8414-a805f398f123%2FUntitled.png)

뭔가 이렇게 하는것보다 더 나아갈것 같은 직감이 든다면 정확합니다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F7addfa81-0efd-4d39-83e0-9d2c983be8b5%2FUntitled.png)

여기에 뭔가 추가되겠지 라는 생각이 든다면 그 생각도 정확합니다.

가장 먼저 home에서 입력받은 데이터를 count 페이지에서 보여주는 부분부터 구현해봅시다.

home.html 부터 시작합시다.  일단 submit버튼 이 누르면 데이터를 count로 전송해야하니 `{% url 'count' %}`를 form의 `action`안에 적어줍시다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F1da77198-16a5-49db-9820-3fc913b18a99%2FUntitled.png)

일단 count로 넘겼는데.. 여기 form에서 넘긴 데이터는 어디로 갈까요?

textarea에 적혀 submit된 내용은 urls.py가 시키는 대로 views.py에 있는 count 함수로 가게 됩니다. 데이터는 넘어왔는데 이 넘어온 데이터를 뭐라고 명명해서 이용해야할지 정해져 있지 않습니다. 이를 위해 views.py안에 count함수 안에 `full_text`라는 변수를 만들어 데이터를 담아봅시다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fdceec0ca-fd5b-4992-acac-3e1a588eeb58%2FUntitled.png)

count 함수 안에 몇가지 내용이 추가되었습니다.

    full_text = request.GET['fulltext']

이 부분은 textarea에서 전송된 정보를 `full_text`라는 변수에 담는 코드입니다. GET이고 POST고 어디서 들어본거 같지만 지금은 넘어갑시다. 앞서 textarea의 name을 'fulltext'라고 지었고, 그렇게 받은 데이터를 full_text에 담는다는 내용입니다.

    return render(request, 'wordcount/count.html', {'fulltext': full_text})

`{'fulltext': full_text}` 라는 내용이 추가되었습니다. 이 부분은 이런 데이터들도 count.html에 넘겨주겠다는 선언입니다. 이부분이 없으면 full_text는 넘어가지 않습니다.

그렇다면 full_text 앞에 있는 'fulltext'는 뭘까요? 이부분은 count.html에서 full_text데이터를 쓸때 'fulltext'라는 이름으로 사용하겠다는 의미입니다. path에서 name을 지정하는 것과 비슷하다 생각하면 됩니다.

이제 다시 count.html로 넘어갑시다.

## view에서 다시 template 으로!

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F37c4fd38-158f-42c3-b5a0-9187131ccc0b%2FUntitled.png)

입력받은 텍스트 밑에 `{{ fulltext }}`를 추가해줍니다. view에서 던져준 데이터를 받아 템플릿에서 보여주는 부분입니다. 앞서 view에서 fulltext라고 이름을 붙여서 던져주었기 때문에 이렇게  소환해야합니다. `{{ }}`는 django에서 넘어온 데이터를 html 파일에서 보여주기 위한 기호입니다.

`{% %}` 과 `{{ }}`는 활용이 다르니 구별해서 써야합니다.

- `{% %}` 과 `{{ }}` 내용 정리
- 중간 테스트

## 다시 view로! count 함수 진화시키기

home에서 입력받아 count 페이지로 넘기는 것까지 처리했으니, 이제 가공하여 가공한 데이터도 넘기는 기능을 만들어 봅시다. 아래 문법에 대한 설명은 생략합니다. 읽어보며 이해해보세요.

1. 총 단어수 세는 기능 구현

        def count(request):
            full_text = request.GET['fulltext']
        
            word_list = full_text.split()
        
            return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total': len(word_list)})

2. 각 단어별로 나온 횟수 세는 기능 구현

        def count(request):
            full_text = request.GET['fulltext']
        
            word_list = full_text.split()
        
            word_dictionary = {}
        
            for word in word_list:
                if word in word_dictionary:
                    # Increase
                    word_dictionary[word] += 1
                else:
                    # add to the dictionary
                    word_dictionary[word] = 1
        
            return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})

이제 count.html 템플릿으로 넘기는 데이터들이 많아졌습니다. 이름을 활용해서 count.html을 수정해봅시다.

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fe433c79e-c156-4271-b0a0-c4c567afa5b2%2FUntitled.png)

{{ total }}은 이제 알아서 넣어서 해보세요. 

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fc4b0649f-89a7-4462-ba2c-f6d3b1fd5627%2FUntitled.png)

단어 카운트 부분에 집중해서 내용을 봅시다.

    {% for word, countTotal in dictionary %}
    {{ word }} - {{ countTotal }}
    <br>
    {% endfor %}

파이썬의 for문을 html파일에서 쓰기 위해서는 `{% %}`을 활용하면 됩니다. 다만 for문이 종료되었다는 내용을 표현해주기위해 `{% endfor %}`를 추가해 주시면 됩니다. `{% for word, countTotal in dictionary %}`와 `{% endfor %}` 사이에 있는 구문은 일반 python 문법과 동일하고, 위 내용은 dictionary의 데이터의 key값과 value값을 각각 가져와 전부 출력하는 구문입니다.

정말 간단히 word를 세주는 앱을 만들어 봤습니다. view에서 어떻게 데이터를 가공하느냐에 따라 더 깔쌈한 어플 제작이 가능해집니다. 그 부분은 여러분에게 맡깁니다.
