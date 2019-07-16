## set

- 집합 연산자로서 '합집합', '교집합', '차집합'



#### 몇가지 팁

- code .  =>  폴더 자체를 vscode로 연다.
- touch app.py  => vscode를 쓰지 않고 app.py를 만들고 싶은 경우



# telegram chatbot

- telegram에서 botfather 검색 -> 인증받은 것에만 '시작' 클릭(**다른 것은 짝퉁이니 주의!**)

- bot name : baambox (이번 예제때 이걸로 입력함)

- user name : baambox_bot (이름이 bot으로 끝나야함, 중복일 경우 다른 것으로 바꿀 것)

- 이렇게 진행하면 token값을 받게된다.  (**유출되지 않도록 주의!**)

- 그리고 api문서 링크가 있으므로 Authorizing your bot부분을 봤음.

  > get 방식 : 주소창에 노출
  >
  > post 방식 : 비밀번호, 아이디 등 노출되지않고 정보 전달

- 아래와 같은 형식을 지켜줄 것.

  > https://api.telegram.org/bot<token>/METHOD_NAME
  >
  > https://api.telegram.org/bot<token>/getMe	이와 같이 인터넷 창에 입력할 경우 정상적인 사용자일 경우 true
  >
  > id : <id> 를 바탕으로 판단하기 때문에 알아둘 것.

- telegram에서 자신의 봇을 검색한 뒤에 시작만 한 상태에서

  > https://api.telegram.org/bot<token>/getUpdate를 하게되면 나의 정보가 뜬다.
  >
  > chat_id : <chat ID>	chat ID 따로 기억

- sendMessage하는 방법

  > https://api.telegram.org/bot<token>/sendMessage?chat_id=<id>&text=안녕하세요

- token 및 id 가리는 방법

  > $ pip install python-decouple
  >
  > 코드에 from decouple import config 추가

  > .env파일 생성 -> TELEGRAM_BOT_TOKEN=''	CHAT_ID=''  토큰값, id 입력후 저장 -> 
  >
  > .gitignore 파일 생성 -> 공식에서 붙여넣고 저장

- webhook과정

  > 서버쪽에
  >
  > @app.route(f'{token}', methods=['POST'])
  >
  > def telegram():
  >
  > ​    return '', 200

- ngrok으로 밖으로 보여줌

  > ngrok을 다운받아서 ~폴더(최상위)로 옮긴다.
  >
  > 실행 -> cmd -> 토큰 입력(맨 처음 한번만)
  >
  > -> ngrok http 5000 입력 (이렇게 켜둔 상태로 둘 것)(포트 맞출 것) -> 나오는 내용 복사

- webhook주소 등록

  > https://api.telegram.org/bot<token>/setWebhook?url=<복사해서 받은 ngrok url>/<token>

- 메아리 찍기

  ```python
  @app.route(f'/{token}', methods=['POST'])
  def telegram():
      # step 1. 데이터 구조 print 해보기
      print(request.get_json())
      from_telegram = request.get_json()
  
      if from_telegram.get('message') is not None:
          # step 2. 그대로 돌려보내기
          chat_id = from_telegram.get('message').get('from').get('id')
          text = from_telegram.get('message').get('text')
          requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
      return '', 200		# 200 : http 연결 성공
  ```

  

## Papago 기능 추가

- 네이버 개발자센터 홈페이지에서 정보 받기

  > clientID : <client ID>
  >
  > client Secret : <client secret>

- slice 개념

  > 0 h 1 e 2 l 3 l 4 o 5	(여기서 숫자는 위치를 나타냄)
  >
  > hello[0:2] => he 까지 출력된다.

- requests : 보내는 것, request : 받는 것(?)

  > requests.get으로는 f스트링 작성하게 되고, 모두에게 보이게 되는 방식

```python
@app.route(f'/{token}', methods=['POST'])
def telegram():
    # step 1. 데이터 구조 print 해보기
#    print(request.get_json())
    from_telegram = request.get_json()

    if from_telegram.get('message') is not None:
        # step 2. 그대로 돌려보내기
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')

        # 한글 키워드 받기

        # /번역 으로 입력이 시작된다면, 파파고로 번역이 동작한다.
        if text[0:4] == '/번역 ':
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            data = {'source': 'ko', 'target': 'en', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            #print(papago_res.json())
            text = papago_res.json().get('message').get('result').get('translatedText') # 여기에 한영 번역 텍스트가 있음

           
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    return '', 200
```



## 배포(deploy)

- 따로 자격증이 있을정도로 까다로운 작업임.

- python anywhere라는 무료사이트를 사용할 예정

- 배포 후에는 Reload해야함

- 또 다른 컴퓨터라고 생각할 것

- 서버에는 파이썬 2가 설치되어있기때문에 파이썬3를 명시할 것.

  > pip3 install python-decouple --user	(어느 서버든 처음 한번만)

- webhook을 ngrok과 연결 더이상 안하고 외부 서버에 항상 연결함. (webhook 다시 등록)

  > https://api.telegram.org/bot<token>/setWebhook?url=<복사해서 받은 python anywhere주소>/<token> (python anywhere의 주소가 **http로 되어있으니 https로 변경!**)

- python anywhere에서 무료회원의 white list가 있어서 동작이 안될 경우, 지원 안해주는 api일 가능성이 있다. 그래서 찾아보고 없으면 돈 내고 등록해야 함.



> indentation error :  tap 오류



