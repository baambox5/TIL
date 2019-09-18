## url 이름 설정

1. ### 하드코딩 URL제거

{% url %} template tag

> \# urls.py
>
> urlpatterns = [
>
> ​    path('', views.index, name='index'),
>
> ]

> \# html파일
>
> \<a href="{% url 'index' %}">[back]</a>
>
> \# pk가 필요한 html파일
>
> \<a href="{% url 'detail' article.pk %}">[DETAIL]</a>

### 문제점

- app이 여러개가 되면, 단순히 url name만 가지고는 어떤 app의 url인지 알 수 없다.



2. ## URL name

> \# urls.py (앱이 여러개가 되었을때)
>
> app_name = 'articles'

> \# html파일
>
> \<a href="{% url 'articles:index' %}">[back]</a>
>
> \# pk가 필요한 html파일
>
> \<a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>

- 지울때 지울지 말지 확인

> \# detail.html
>
> \<a href="{% url 'articles:delete' article.pk %}" onclick="return confirm('진짜 지울거야?')">[DELETE]</a>



- 쿠키와 세션

  쿠키 : 사용자쪽에서 가지고 있는 것

  세션 : 서버쪽에서 가지고 있는 것,

- URI(Uniform Resource Identifier)

  - 통합 자원 식별자
  - 인터넷에 자원을 나타내는 유일한 주소
  - 인터넷에서 요구되는 기본 조건으로서, http에 항상 붙어다닌다.

  - 이 안에 URL, URN이 포함되어 있다.

- URL

  - 인터넷 상에서 자원이 어디 있는지 알려주기 위한 규약

- URN은 서버내부의 고유 주소로 평소에 사용할 일이 없다.



### 예제

ex) https://www.google.com

- 서버주소 (URL이면서 URI)

ex) https://github.com/baambox5/TIL/blob/master/03_django/manage.py

- 주소 + 디렉토리 파일의 주소(자원의 위치)
- URL이면서 URI

----------

ex) https://www.google.com/search?q=삼성

- 주소 + 특정 문자열(query string) (`search?q=`)
- search까지가 URL + `q=삼성`이라는 식별자가 필요하므로 URI이지만 URL은 아니다.



## REST

- 소프트웨어 이론. 규약은 아니지만 지키면 좋음.

1. URI는 정보의 자원을 표현해야 한다.
2. 자원에 대한 행위는 HTTP Method로 표현한다.



Django에서는 GET POST PATCH DELETE 중에 GET POST만 사용(프레임워크에 따라 사용할 수도 있음.)

실제로 HTTP에서는 공식적으로 GET POST이 사용된다.



- 같은 주소로 들어가는데 GET이냐 POST이냐에 따라 행동을 다르게 한다.
- (new[GET] + create[POST])
- GET articles/create/ 글을 작성하는 페이지
- POST articles/create/ 글이 실제로 작성
- form tag에 action이 없다면, 현재 머물고 있는 URL로 요청을 보낸다.



## Model Instance Method

### 1. `get_absolute_url()`

- 특정 모델에 대해 detail view를 작성할 경우, detail url을 완성하자마자 사용하는 것을 권장한다.
- 반복되는 코드가 줄고 보다 간결해진다.



## URL Reverse를 수행하는 함수들

### 1. reverse()

- 리턴 값: string(문자열)

```python
reverse('articles:index') # '/articles/'
```

### 2. redirect()

- 리턴 값: HttpResponseRedirect(객체)
- 내부적으로 `resolve_url()`을 사용
- view 함수에서 특정 url로 돌려보내고자 할 때 사용

```python
redirect('articles:article')
# <HttpResponseRedirect status_code=200, "text/html; charset=utf-8, url="/articles/">
```

### 3. url template tag ({% url %})

- 내부적으로 `reverse()`를 사용



### `redirect(모델 인스턴스)`를 통해서 모델 인스턴스의 get_absolute_url()함수를 자동으로 호출