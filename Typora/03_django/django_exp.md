# django 실습

### message echo

- views.py

>  def throw(request):
>
> ​    return render(request, 'throw.html')

> def catch(request):
>
> ​    message = request.GET.get('message')	# GET은 대문자!, message는 key값으로 전달받음.
>
> ​	context = {'message': message,}
>
> ​    return render(request, 'catch.html')

#### html

- form tag를 활용한다.

> \<form action="/catch/" method="GET">   /~~/ 여기서 처음 /는 필수, post방식은 마지막 / 필수
>
>   <label for="message">THROW</label>
>
>   <input type="text" id="message" name="message">
>
>   <input type="submit">
>
> </form>

> catch에서 보낸 {{ message }}를 받았습니다.



pprint(request.META) => request의 모든 정보



$ pip install requests



- ##### ASCII-ART

> def result(request):
>
> ​    \# 1. art에서 form으로 보낸 데이터를 받는다.
>
> ​    word = request.GET.get('word')
>
> ​    
>
> ​    \# 2. ARTII API 폰트 리스트로 요청을 보내 응답을 text로 받는다.
>
> ​    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
>
> 
>
> ​    \# 3. str을 list로 바꾼다.
>
> ​    fonts = fonts.split('\n')
>
> 
>
> ​    \# 4. fonts list 안에 들어있는 요소 중 하나를 선택해서 변수에 저장.
>
> ​    font = random.choice(fonts)
>
> 
>
> ​    \# 5. 위에서 만든 word와 font를 가지고 다시 요청을 만들어서 보내 응답결과를 받는다.
>
> ​    response = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
>
> 
>
> ​    context = {'response': response,}
>
> ​    return render(request, 'result.html', context)



- get방식의 경우 짧은 text정도밖에 보낼 수가 없다.



#### CSRF 사이트간 요청 위조

- 웹 어플리케이션 취약점 중 하나로 사용자가 자신의 의도와 무관하게 공격자가 의도한 행동을 해서 특정 웹페이지의 보안을 무력화시키거나, 수정, 삭제 등의 강제적인 작업을 하게하는 공격 방법.
- django는 최소한의 안전장치를 위해 자신이 부여한 랜덤 hash 값을 token으로 부여한다. 이 token 값이 없는 요청은 잘못된 요청이라고 판단하여 접근을 거부한다. (403 error)



## static 정적파일

- image / css / js 파일과 같이 해당 내용이 고정되어 응답을 할 때, 별도의 처리없이 그대로 보여주면 되는 파일들.

> {% load static %}
>
> 이것을 맨 위에 넣어줘야함.

> \<img src="{% static 'images/avocado.jpg' %}" alt="static_image">
>
> 위와 같이 경로에서 static은 제외하고 경로 지정해주면 된다.
>
> static 폴더를 만들어줘야함!
>
> 그 안에 images, stylesheets 등의 파일을 넣음.



## Django namespace(여러 앱 사용시)

- ##### url 등록

> # 프로젝트 urls.py
>
> from django.contrib import admin
>
> from django.urls import path, include	# include 추가
>
> 
>
> urlpatterns = [
>
> ​    path('utilities/', include('utilities.urls')),
>
> ​    path('pages/', include('pages.urls')),
>
> ​    path('admin/', admin.site.urls),
>
> ]

> # app url.py
>
> from django.urls import path
>
> from . import views	# . 은 명시적인 표현을 위함.
>
> urlpatterns = [
>
> ​    \# 원래 app url은 아래로 작성해나간다.
>
> ]

- ##### templates, static폴더 안에서 각각 앱에 해당하는 폴더를 나눠줘야 함!



{% extends 'base.html' %} 가 가장 최상단에 있어야 함!



$ pip freeze > requirements.txt	가상환경 리스트 만들기

$ pip install -r requirements.txt	가상환경 리스트 설치(**가상환경을 만들고 설치할 것!**)