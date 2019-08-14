import random
from datetime import datetime
from django.shortcuts import render


# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'index.html') # render()의 첫번째 인자도 반드시 request


def introduce(request):
    return render(request, 'introduce.html')


def dinner(request):
    menu = ['족발', '짬뽕', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick,}
    return render(request, 'dinner.html', context)


def image(request):
    url = 'http://picsum.photos/500/500.jpg'
    context = {'url': url}
    return render(request, 'image.html', context)


def hello(request, name):
    menu = ['족발', '짬뽕', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'name': name, 'pick': pick,}
    return render(request, 'hello.html', context)


def intro(request, name, age):
    context = {'name': name, 'age': age,}
    return render(request, 'intro.html', context)


def multi(request, num_1, num_2):
    res = num_1 * num_2
    context = {'res': res,}
    return render(request, 'multi.html', context)


def round_width(request, radius):
    res = radius**2 * 3.14
    context = {'res': res,}
    return render(request, 'round_width.html', context)


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
    return render(request, 'template_language.html', context)


def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {'result': result,}
    return render(request, 'gwangbok.html', context)