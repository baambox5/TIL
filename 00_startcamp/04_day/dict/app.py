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

    # 좀 더 짧은 코드(위의 for문 3줄을 아래 한 줄로 만들 수 있다.)
    matched = len(set(winner) & set(numbers))

    if len(numbers) == 6:
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
    else:
        result = '번호가 6개가 아닙니다.'
    return render_template('lotto_result.html', winner=winner, numbers=numbers, result=result)