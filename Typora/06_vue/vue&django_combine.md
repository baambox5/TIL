# vue&django_combine

djnago쪽 설치

> $ pip install djangorestframework
>
> $ pip install djangorestframework-jwt
>
> $ pip install django-cors-headers



vue쪽 plugin 설치

> $ npm i vue-session
>
> $ npm i jwt-decode



## 데이터 전달 흐름

1. Vue -> Django
   - POST 유저 정보를 통해 로그인 시도
2. Django 내
   - Access Token(JWT)
3. Django -> Vue
   - 발급된 JWT를 전달
4. Vue -> Django
   - Authorization header에 JWT를 붙여서 요청
5. Django 내
   - JWT를 해석해서 정보 전송
6. Django -> Vue
   - response



## 과정

### 0. Django

- 회원 가입

### 1. Vue -> Django

- 로그인 정보(credentials)를 django 서버로 보냄

### 2. Django

- Vue에서 받은 유저정보에 해당하는 고유한 Web Token 발급

### 3. Django -> Vue

- 해당 유저에 대한 토큰을 Vue로 보냄

### 4. Vue

- Django에서 받은 토큰을 vue-session을 통해 저장(이 시점부터 vue에서는 로그인 성공 상태)

### 5. Vue -> Django

- vue-session에 저장된 토큰을 가지고 Django에 로그인 요청

### 6. Django

- 최초로 보낸 토큰과 일치하는지 여부를 확인(django session에 저장된 토큰 == 요청자의 토큰)

-----------

.start() 를 통해 `session-id`:`sess`+`Date.now()`가 만들어짐

`.set()` 을 통해 `jwt: jwt 값` 이 만들어짐

-------

## Session Reference

### this.$session.start() 

- session-id 초기화. 만약 세션 없이 저장하려고 하면 vue-session 플러그인이 자동으로 새로운 세션을 시작.



### this.$session.set(key,value)

- session에 해당 key에 맞는 값을 저장.



### this.$session.has(key) 

- key(JWT)가 session에 존재하는지 여부를 확인



### this.$session.destroy() 

- 세션을 삭제

--------------------

## Vue lifecycle

### 1. Vue instance 생성 (create)

### 2. DOM에 부착 (mounted)

### 3. 업데이트 (update)

### 4. 사라짐 (destroy)



- 토큰을 Autohrization header에 붙여서 보낼때 JWT + 공백을 앞에 붙여서 보낸다. (`""`는 사용할 필요 없음)

----------

### FormData

- 기존 키에 새로운 값을 추가하거나 키가 없는 경우 새로운 키를 추가. (`FormData.append()`)
- `FormData.append(name, value)`
- name : value에 포함되는 데이터 필드 이름
- value는 필드 값