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

> $ vue ui
>
> vuex 검색해서 설치



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

----------------

### `splice()`

- 배열의 기존 요소를 삭제 혹은 교체하거나 새 요소를 추가하여 배열의 내용을 변경
- 문법
  - `Array.splice(시작 index, 삭제할 요소 수, 배열에 추가할 요소)`
  - `splice(start, deleteCount, [item1, item2, item3, ...])`
    1. start
       - 배열의 변경을 시작할 인덱스
       - 배열의 길이보다 큰 값이면 시작인덱스는 배열의 길이로 설정
       - 음수인 경우 배열의 가장 마지막에서 시작
       - 절대 값이 배열의 길이보다 큰 경우는 0으로 설정.
    2. deleteCount
       - 배열에서 제거할 요소의 수
       - 생략할 경우 start부터 모든 요소를 제거
       - 0 이하인 경우 어떤 요소도 삭제하지 않음. 이때는 최소한 하나의 추가할 새로운 요소 지정.
    3. item1, item2
       - 배열에 추가할 요소
       - 아무 요소도 지정하지 않으면 요소를 제거만 한다.
       - 즉, **추가할 요소를 지정하지 않으면 원본 배열의 특정 인덱스에서 몇개의 요소를 삭제**할지 정한다.

----------------

### updated

- 타입 : function
- 상세 :
  - 데이터가 변경되어 DOM이 re-render 되고, patch 되면 호출된다. (DOM 변화에 반응)
  - DOM의 변화는 일반적으로 데이터의 변경에 의해 re-render 되는 시점에 일어난다.
  - 데이터의 변화(상태의 변화)에 반응하기 위해서는 computed나 watch를 사용하는 것이 좋다.

-------------

## Vuex

- State 관리를 위해 탄생
- 컴포넌트 간의 통신 혹은 데이터 전달을 유기적으로 관리
- 컴포넌트 간의 통신 혹은 이벤트 등의 관계를 한 곳에서 관리하기 쉽게 구조화



현재 todo 프로젝트에서는 Auth 정보(로그인 혹은 로그아웃)은 django로 요청을 보낼때 항상 필요하기 때문에, 요청을 수행하는 모든 컴포넌트에서 알고 있어야 하고, 그 정보를 내가 필요한 순간에 활용할 수 있어야 한다.



1. state
   - 상태(데이터)
2. Getters
   - computed
3. Mutations
   - methods
   - state를 변경하기 위해서 반드시 동기적인 method만 사용 가능
   - 첫 번째 인자는 항상 state, 호출은 commit으로 된다.
4. Actions
   - 모든 methods
   - 비동기 처리가 가능한 methods
   - mutations와 구분된 이유는 다양한 컴포넌트에서 vuex를 통해 상태관리, 메서드 호출 등을 하게 될텐데 그때 동기와 비동기를 구분하기 위해.
   - 첫 번째 인자는 항상 context(state/commit/dispatch 등), 호출은 dispatch로 된다.

-----------

vuex는 `vue-session`의 대체가 아니고 서로 하는 일이 다르다.

vuex는 메서드와 data의 대체라고 생각하자.