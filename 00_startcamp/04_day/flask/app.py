from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

# render template
@app.route('/')
def hello():
#    return 'Hello World!'
    return render_template('index.html')


@app.route('/ssafy/')
def ssafy():
    return 'This is SSAFY!'


@app.route('/dday/')
def dday():
    # 오늘 날짜
    today_time = datetime.now()
    # 수료 날짜
    endgame = datetime(2019, 11, 29)
    # 수료날짜 - 오늘 날짜
    dday = endgame - today_time
    return f'{dday.days} 일 남았습니다.'


@app.route('/html/')
def html():
    return '<h1>This is HTML TAG</h1>'


@app.route('/html_line/')
def html_line():
    return """
    <h1>여러 줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """


# variable routing
@app.route('/greeting/<name>/')
def greeting(name):
#    return f'반갑습니다! {name}'
    return render_template('greeting.html', html_name=name)

@app.route('/cube/<int:number>/')
def cube(number):
    # 연산을 모두 끝내고 변수만 cube.html 로 넘긴다.
    number3 = number**3
#    return f'{number}의 세제곱은 {number**3}입니다.'
    return render_template('cube.html', html_number=number, html_number3=number3)


@app.route('/lunch/<int:people_count>/')
def lunch(people_count):
    menus = ['삼계탕', '햄버거', '떡볶이', '치킨', '냉면', '사탕', '짜장면']
#    return f'{random.choices(menus,k=people_count)}'
    return f'{random.sample(menus,people_count)}'
            

@app.route('/movie/')
def movie():
    movies = ['토이스토리4', '스파이더맨', '알라딘', '기생충']
    return render_template('movie.html', movies=movies)


@app.route('/ping/')
def ping():
    return render_template('ping.html')


@app.route('/pong/')
def pong():
    # print(dir(request))
    name = request.args.get('data')    # 안녕하세요
    return render_template('pong.html', name=name)


# https://search.naver.com/search.naver?query=
@app.route('/naver/')
def naver():
    return render_template('naver.html')


@app.route('/google/')
def google():
    return render_template('google.html')


@app.route('/vonvon/')
def vonvon():
    return render_template('vonvon.html')


@app.route('/vonvon_char/')
def vonvon_char():
    charactor = ['차분함', '성격급함', '낙천적임', '광기있음', '음침함', '친절함', '항상 즐거움']
    user_name = request.args.get('user_name')
    selected_charactor = random.sample(charactor, 3)
    return render_template('vonvon_char.html', user_name = user_name, charactor = selected_charactor)