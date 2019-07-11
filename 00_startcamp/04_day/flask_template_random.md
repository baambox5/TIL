## flask

> export FLASK_APP=hello.py 로 환경변수 설정을 했지만, 기본값이 export FLASK_APP=app.py
>
> 때문에 코드파일명을 app.py로 저장했을경우 환경변수 설정 없이도 flask run만으로도 동작함.

- pylint경고 : 다른 기본 변수와 중복 경고

  > datetime끼리는 연산 가능

- 함수나 클래스끼리는 두줄 띄는게 convention



## variable routing(변수 라우팅)

> def greeting(name):
>
> ​    return f'반갑습니다! {name}'

> @app.route('/greeting/\<string:name>/') 이 기본세팅이라서 <string:> 부분 생략 가능 

> rm -rf ~/.bash_profile 지우는 명령어



## render template

- 서버에서 매칭된 template을 불러와서 client에게 보여준다.
- app.py와 같은 경로에 templates 폴더가 있어야 가져올 수 있다.



- html 기초 단축키 : 맨 처음에 작성할때 !+tap입력하면 기본 구조가 만들어진다.
- 기본적으로 연산은 서버에서, 보여주는 것은 template에서



#### jinja2 template

> return render_template('cube.html', html_number=number3)
>
> 괄호 오른쪽에 있는 html_number를 cube.html에 넘김.
>
> html_number3와 number3의 이름이 같아도 상관없음

> template에서
>
> ```html
> <body>
> 
> ​    {{ html_number }}의 세제곱은 {{ html_number3 }}입니다.
> 
> </body>
> ```

> ```html
> {% if html_name == '병권' %}
> 
> ​    <h2>{{ html_name }} 왔냐?</h2>
> 
> {% else %}
> 
> ​    <h2>누구냐</h2>
> 
> {% endif %} 
> ```
>
> ```html
> {% for user in users %}
> 	<li><a href="{{ user.url }}">{{ user.username }}</a></li>
> {% endfor %}
> ```
>
> 와 같은 형태로 조건문(**endif를 해줘야 함**), 반복문(**endfor를 해줘야 함**) 사용

> <!-- 보이는건 {{}} 안에 넣기 --> 와 같은 html 주석에서 {{}}부분은 jinja template에서는 주석이 아니기 때문에 {# #}로 바꿔야 제대로 주석 처리가 된다.



### random함수

> - Use the **random.sample** function when you want to choose multiple random items from a list without including the duplicates.
> - Use **random.choices** function when you want to choose multiple items out of a list including repeated.

> - **random.sample** 함수는 랜덤이지만 요소간의 중복을 허용하지 않기 때문에, 리스트의 크기(요소 수)를 초과할 경우 에러가 발생함.
>
>   ex) 에러 : 8개의 요소가 있는 리스트에서 랜덤으로 9개 뽑으라고 할 경우
>
> - random.choices 함수는 요소간의 중복을 허용하기 때문에, 요소 수의 제한이 없음.



## flask request & response(페이지에서 자료 주고 받기)

- 보낼때 이름태그(name)를 꼭 만들어줄 것.

  ```html
  ping.html
  <input type="text" name="data">
  <input type="submit" value="퐁!!">
  ```

- html은 ""가 convention



- dictionary형태로 request가 보내짐



```html
 <form action="https://www.google.com/search?">
```

- 여기서 ?를 지워도 이상없이 동작한다. ?가 구역을 구분하는 단위이기 때문에



- \<br> : break line (줄 바꿈)	=	\</br>

 



## Dictionary

```python
# 딕셔너리 만들기 - 1
lunch = {
    '중국집': '02-345-1245'
}

# 딕셔너리 만들기 - 2
dinner = dict(중국집='02', 일식집='031')


# 딕셔너리에 내용 추가하기
lunch['분식집'] = '031-123-2622'
# print(lunch)

# 딕셔너리 내용 가져오기
idol = {
    'bts': {            # key value를 점점 아래쪽으로 엔터쳐서 내리는 것을 권장
        '지민': 25,
        'RM': 24
    }
}
# RM의 나이는?
# 아래 두 줄의 경우 같은 동작을 하는 코드임.
# .get의 경우 : 없는 key값의 경우 None을 출력 => 서버에서는 이것만 사용
# []형식의 경우 : 없는 key값의 경우 key error발생 => 서버 꺼짐 
idol['bts']['RM']
idol.get('bts').get('RM')
```



```python
#딕셔너리 반복문 활용

lunch = {
    '중국집': '02-345-1245',
    '분식집': '031-123-2622',
    '일식집': '089-5124-3256'
}

# 기본 활용
for key in lunch:
    print(key)
    print(lunch[key])

# key, value 둘다 가져옴 .items()
for key, value in lunch.items():
    print(key, value)

# value 만 가져오기 .values()
for value in lunch.values():
    print(value)

# key 만 가져오기 .keys()
for key in lunch.keys():
    print(key)
```



- JSON Viewer : chrome 확장프로그램



## lotto(예제)

```python
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# 로또 회차 / 내 번호 입력페이지
@app.route('/lotto_check/')
def lotto_check():
    return render_template('lotto_check.html')

# 결과페이지
@app.route('/lotto_result/')
def lotto_result():
    # 회차 번호를 받아온다.
    num = request.args.get('num')
    # 동행복권에 요청을 보내 응답을 받는다.
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
    # json 형태로 바꿔준다. (우리가 크롬에서 보고있는 결과와 동일한 모습)
    lotto = res.json()

    # 당첨번호 6개만 가져오기
    winner = []
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])

    # 내 번호 list 만들기
    numbers = []
    for num in request.args.get('numbers').split():
        numbers.append(int(num))
    
    # 등수 가리기(몇 개 맞았는지 교집합이 필요)
    matched = 0
    # 내 번호 요소를 뽑아서 당첨번호 리스트에 있는지 확인.
    for num in numbers:
        if num in winner:
            matched += 1
    if matched == 6:
        result = '1등입니다!'
    elif matched == 5:
        if lotto['bnusNo'] in numbers:
            result = '2등입니다!'
        else:
            result = '3등입니다!'
    elif matched == 4:
        result = '4등입니다!'
    elif matched == 3:
        result = '5등입니다!'
    else:
        result = '꽝입니다!'
    return render_template('lotto_result.html', winner=winner, numbers=numbers, result=result)
```

