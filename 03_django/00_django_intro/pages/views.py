import random
from datetime import datetime
from pprint import pprint
import requests
from django.shortcuts import render


# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'pages/index.html') # render()의 첫번째 인자도 반드시 request


def introduce(request):
    return render(request, 'pages/introduce.html')


def dinner(request):
    menu = ['족발', '짬뽕', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick,}
    return render(request, 'pages/dinner.html', context)


def image(request):
    url = 'http://picsum.photos/500/500.jpg'
    context = {'url': url}
    return render(request, 'pages/image.html', context)


def hello(request, name):
    menu = ['족발', '짬뽕', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'name': name, 'pick': pick,}
    return render(request, 'pages/hello.html', context)


def intro(request, name, age):
    context = {'name': name, 'age': age,}
    return render(request, 'pages/intro.html', context)


def multi(request, num_1, num_2):
    res = num_1 * num_2
    context = {'res': res,}
    return render(request, 'pages/multi.html', context)


def round_width(request, radius):
    res = radius**2 * 3.14
    context = {'res': res,}
    return render(request, 'pages/round_width.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피', '깐풍기', '라조육',]
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'bean',]
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'pages/template_language.html', context)


def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {'result': result,}
    return render(request, 'pages/gwangbok.html', context)


def throw(request):
    return render(request, 'pages/throw.html')


def catch(request):
    # pprint(request)
    # pprint(request.META)
    message = request.GET.get('message')
    context = {'message': message,}
    return render(request, 'pages/catch.html', context)


def art(request):
    return render(request, 'pages/art.html')


def result(request):
    # 1. art에서 form으로 보낸 데이터를 받는다.
    word = request.GET.get('word')
    
    # 2. ARTII API 폰트 리스트로 요청을 보내 응답을 text로 받는다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    # 3. str을 list로 바꾼다.
    fonts = fonts.split('\n')

    # 4. fonts list 안에 들어있는 요소 중 하나를 선택해서 변수에 저장.
    font = random.choice(fonts)

    # 5. 위에서 만든 word와 font를 가지고 다시 요청을 만들어서 보내 응답결과를 받는다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {'response': response,}
    return render(request, 'pages/result.html', context)


def user_new(request):
    return render(request, 'pages/user_new.html')


def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name': name, 'pwd': pwd,}
    return render(request, 'pages/user_create.html', context)


def static_example(request):
    return render(request, 'pages/static_example.html')