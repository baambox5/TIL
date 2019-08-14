# django

- 100% 파이썬으로 짜여진 프레임워크
- 다른 것들(react, vue 등)과 호환이 잘 됨.
- 프레임워크를 써서 안전.
- 코드가 간결함.
- 다양한 운영체제에서 작성 가능
- 다소 독선적임. (프레임워크가 하라는 데로 하면 코드가 간결해짐)
- 관용적인 프레임워크는 다리 역할만 함.(개발자가 손 봐야할 것이 많음)



##### 의존성

- 본인의 컴퓨터에서 잘 작동하던 프로그램도, 다른 프로그램에 설치했을때 잘 동작하리라는 보장이 없음.
- 파이썬도 같은 버전, 같은 모듈을 쓴다는 보장이 없다.
- 특정 프로그램만을 실행하기 위한 파이썬 환경을 따로 만들어서, 그 환경 속에서만 모듈을 관리하고, 앱을 실행시키기 위해 가상환경을 설정한다.
- 다른 앱을 실행시키는 일이 생기면 그 가상환경을 빠져나와 다른 환경을 만드는 방식으로 진행한다.



#### 가상환경 만들기

> $ python -m venv (가상환경 경로 + 이름)
>
> => (**여기서 venv는 이전에 단축어로 지정한 것과는 완전히 다른 의미이므로 주의!**)
>
> ex) $ python -m venv ssafy (ssafy라는 이름의 가상환경이 만들어짐. 보통 경로는 그 위치에 가서 만든다)

- gitignore에서 django와 vs-code로 만들면 된다. (만들때 .vscode/*를 .vscode로 바꿀 것)

> $ python -m venv venv (venv라는 것으로 가상환경을 만듬)
>
> $ source venv/Scripts/activate => (실행)
>
> $ python -m pip install --upgrade pip => (pip update)
>
> $ deactivate => (종료)



- vs code에서 설정

> f1또는 ctr+shift+p에서 interpreter 검색
>
> 만들어둔 python을 엔터 => 좌하단에서 버젼 확인 가능



> settings 검색 => "terminal.integrated.cwd": "${workspaceFolder}", 추가
>
> shortcut 검색 => integrate => terminal.newInActiveWorkspace 에 ctr+` 넣기



- django 설치

> vs code에서 $ pip install django

- django 버젼 확인

> $ python -m django --version

- django 프로젝트 만들기

> $ django-admin startproject django_intro .
>
> (마지막에 . 을 안 붙일경우 폴더 안에 또 폴더가 생긴다.)



- ##### django 서버 실행

> manage.py랑 같은 위치에서
>
> $ python manage.py runserver



- 기본 파일들 설명
  - \__init__.py : 모듈에 관한(?) 현재는 별로 쓸 일이 없음.
  - settings.py : 장고의 모든 환경이 저장되어 여기서 작업을 많이 함.
  - urls.py : url관련된 부분을 작성할 예정. 사용자의 요청을 가장 처음에 받음.
  - wsgi.py : aws 관련이라 마지막에 배포할 시에 설정.



- 기존의 MVC가 장고에서는 MTV. 이름만 다르다고 생각하면 된다.
  - 그래서 view가 controller
  - 보여지는 것은 template
  - 데이터를 관리하는 것은 model



- ##### 앱 만들기

> $ python manage.py startapp pages
>
> pages라는 앱을 만든다.(복수형으로 이름짓는게 convention)



- 앱의 기본 파일 설명 
  - admin.py : 관리자 페이지용(미리 기본적인 부분은 만들어져 있다!)
  - apps.py : 앱의 정보. 안 건들 예정.
  - models.py : 데이터베이스할때 추후 다룰 예정.
  - tests.py : 테스트 코드 작성할 경우
  - views.py : 중간 관리자 역할



- ##### 앱 생성 후 등록

  - settings.py에서 INSTALLED_APPS에 'pages', (제한될 가능성) 혹은 'pages.contrib.PagesConfig', (정식 등록)를 추가. trailing comma(',')가 하나라도 붙어 있는게 convention
  - app 등록 순서
    	1. local apps
     	2. Third party apps
     	3. Django apps
  - Internationalization == I18n으로 보통 단축해서 말함
  - Timezone이 약속되어 있다.
  - USE_TZ이 True로 되어 있으면, 접속자의 위치에 맞는 시간을 설정해준다. (왠만하면 건들지 말 것)



- #### 기본 작성

  1. 앱의 views에서(만들고자 하는 view 함수 작성)

     > def index(request): 
     >
     > => 첫번째 인자는 반드시 request
     >
     > return render(request, 'index.html')
     >
     > => render()의 첫번째 인자도 반드시 request.	templates의 html파일을 찾는다.

  2. 프로젝트의 urls에서 (views에서 만든 함수에 주소를 연결)

     > from pages import views
     >
     > => 생성한 app pages 폴더 안의 views.py 파일
     >
     > urlpatterns = [ path('index/', views.index), ]
     >
     > => url 경로 마지막에 /를 붙이는 습관(index라는 주소)

  3. app폴더에서 templates 폴더를 만들고, 그 안에 html 파일을 만든다. (해당 view함수가 호출될때 보여질 페이지)

  4. import style guide

     ​	1) standard library (내장함수)

     ​	2) third party (외장함수)

     ​	3) Django

     ​	4) local django



- extension django 설치

  - 여기서 repository로 들어가서 코드들 settings(json)에 복사

  - beautiful soup 설치 => repository 들어가서 코드들 마찬가지로 settings(json)에 복사

    > "[django-html]": {
    >
    > ​    "editor.tabSize": 2
    >
    >   },
    >
    > => 이것도 추가할 것.



- #### variable routing (동적라우팅)

  - 주소 자체를 변수처럼

    - view에서

      > def hello(request, name):	=> 여기서 name은 url에서의 <name>과 맞춰줘야 함.
      >
      > ​    context = {'name': name}
      >
      > ​    return render(request, 'hello.html', context)

    - url에서

      > path('hello/<name>/', views.hello), => **<name>은 변수처럼**

    - hello.html파일에서

      > \<h1>안녕하세요, {{ name }}</h1>
      >
      > \<h1>오늘 먹을 음식은 {{ pick }}입니다.</h1>



- Django Template Language (DTL)

  - django template에서 사용하는 내장 template system이다.

  - 조건, 반복, 변수 치환, 필터 등 많은 기능을 제공한다.

  - jinja template와 유사하지만, 좀 더 발전된 형태로 보면 된다.

  - forloop는 DTL for문 안에서 자동으로 생기는 객체

    > <h3>1. 반복문</h3>
    >
    > {% for menu in menus %}
    >
    > <p>{{ menu }}</p>
    >
    > {% endfor %} => 꼭 닫아줄 것.

    > {% for user in empty_list %}
    >
    > <p>{{ user }}</p>
    >
    > {% empty %} <!-- 비어있으면, 아래쪽이 실행, 그렇지 않으면 위쪽이 실행 -->
    >
    > <p>현재 가입된 유저가 없습니다.</p>
    >
    > {% endfor %}

  - <=, >=, ==, !=, >, <, in, not in, is 모두 사용 가능

  - 이미 정의되어 있는 변수 호출은 {% %}를 사용한다.