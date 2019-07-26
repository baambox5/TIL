# # .update()
# a = {}

# # 1
# a.update(key='value')

# # 2
# a.update({key: value})

# # .env 환경변수 세팅 (python-decouple)




# # .py

# # 네이버 요청하는 법
# # 1-1 기본 설정
# import requests
# from decouple import config

# CLIENT_ID = config(NAVER_CLIENT_ID)
# CLIENT_SECRET = config(NAVER_CLIENT_SECRET)
# HEADERS = {'X-Naver-Client-Id': CLIENT_ID, 'X-Naver-Client-Secret': CLIENT_SECRET}

# # 1-2 요청보내기
# url = 'https://openapi.naver.com/v1/search/blog.json'
# address = f'{url}?query={movieNm}'
# response = requests.get(address, headers=HEADERS).json()


a = float('0.00003')
print(type(a))
b = 8.0002
d = {'ab': b}

print(d)

