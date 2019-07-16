# html

<!DOCTYPE html> : html 선언
<html>
    <head>	 <!--사용자 눈에 보이지 않는 로딩용 코드-->
        <meta charset="UTF-8">
        <title>여기는 네이버입니다.</title>	<!-- 맨 위의 창 제목-->
    </head>
    <body>	<!-- 사용자 눈에 보이는 부분-->
        <h1>
            H1 태그입니다.
        </h1>
        <h2>
            HTML & CSS 맛보기
        </h2>
    </body>
</html>

</!doctype>



ctr+shift+s : 검사





## github 도메인 설정

- new repository -> baambox5.github.io(자신의 유저네임.github.io) 로 이름 설정



## Flask & Django(spring, ruby on rails) - Server

- 언어에 따라 플랫폼이 있다.



### Flask

- flask 검색으로 나오는 홈페이지에서 하라는 데로 따라할 것.

- bash에 대한 환경변수 설정(숨김파일) : ~/.bash_profile을 수정

  > export FLASK_APP=hello.py(원하는 내용(**공백 없어야함!**))
  >
  > terminal을 리셋(source ~/.bash_profile)

- debug mode 켜는 방법(실시간 수정을 위해서):

  > ~/.bash_profile에서 export FLASK_ENV=development
  >
  > terminal을 리셋(source ~/.bash_profile)

- 주소창 뒤쪽에 더 추가하기

  > @app.route('/ssafy/')	# /원하는 주소명/
  >
  > def ssafy():					# def 하는 명칭을 앞쪽에서 정의하지 않은 것으로 해야 함
  >
  > ​    return "This is ssafy!"