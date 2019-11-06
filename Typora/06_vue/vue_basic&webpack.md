## v-model

- input tag의 value - **View** <-----> v-model <-----> data (**VM**)



### computed

- 미리 계산된 값을 반환.
- 종속 대상을 따라 저장(캐싱)되는 특성이 있다.
- 연산이 많이 필요한 경우 템플릿 안에서 연산 표현식을 사용하는 것보다 computed를 사용하는 것을 권장.
- 미리 계산된 값을 가져오는 것으로 ()를 붙여 호출하지 않는다.
- `{{ newTodo.split('').reverse().join('') }}`

```vue
computed: {
	reversedNewTodo: function() {
		return this.newTodo.split('').reverse().join('')
	}
}
```

-----------

- Session storage: 브라우저가 닫힐때까지만 유지
- Local storage: 브라우저가 닫혀도 유지
  - localStorage.getItem(key) : 가져오기
  - localStorage.setItem(key, value) : 저장하기
  - localStorage.removeItem(key) : 삭제하기

-------------------

### Watch

- Vue 인스턴스의 data 변경을 관찰하고 이에 반응
- 데이터 변경에 대한 응답으로 비동기 또는 시간이 많이 소요되는 조작을 수행하려는 경우에 적합.
- 특정 데이터가 변경되었을 때 정의한 함수를 실행.

-----------

## v-if / v-show

- `v-if` : 조건에 맞지 않으면 렌더링 자체를 하지 않음
- `v-show` : 조건과 관계 없이 일단 렌더링 후에, 조건에 맞지 않으면 CSS display 속성을 토글해서 숨겨버림.

-------------

### `v-bind:` -> `:`

### `v-on:` -> `@`

------------------

## computed vs watch

- **computed** : 계산해야 하는 목표 데이터를 정의하는 방식 (선언형 프로그래밍)
- **watch** : 감시할 데이터를 지정하고 그 데이터가 바뀌면 특정 함수를 실행하라는 방식(명령형 프로그래밍)

--------------

## 컴포넌트

- "소프트웨어 개발에서 독립적인 단위 모듈"

- 대체로 컴포넌트는 특정 기능이나 관련된 기능의 조합으로 구성되는데, 프로그래밍 설계에서 시스템은 모듈로 구성된 컴포넌트로 나뉜다.

- VUE - "기본 HTML 엘리먼트를 확장하여 재사용 가능한 코드로 캡슐화하는 것"

- 컴포넌트 안에서는

  ```vue
  data: function() {
  	return {
  		counter: 0
  	}
  },
  ```

  와 같이 구성해야한다.



### 컴포넌트 naming convention

- 컴포넌트의 첫번째 인자는 태그이름, 두번째 인자는 속성들을 넣어준다.

1. kebab-case => `todo-list`
   - 호출할 때 : `<todo-list></todo-list>` 케밥케이스 태그로만 호출 가능
2. paskalCase => `TodoList`
   - 호출할 때 : `<todo-list></todo-list>` / `<TodoList>` 둘다 호출 가능.
   - 단, DOM에서 직접 작성할 때는 케밥케이스만 가능.

- 그래서 vue는 모두 소문자여야하고, 하이픈을 포함하는 규칙을 따르는 것을 권장한다.



### props

- 컴포넌트를 재생산할때 컴포넌트에서 사용할 변수를 부모에서 내려주게 되는데, 이를 `props` 라고 한다.
- 반복되는 컴포넌트에 서로 다른 정보가 들어가야할 때 사용.
- 하위(자식)에서 상위(부모) 데이터를 직접 참조해선 안되고 실제로도 안된다.
- `props` 옵션을 통해 부모 -> 자식으로 데이터를 전달.
- 전달하려고 하는 **데이터의 이름을 태그 내의 속성**으로, 내용을 속성 값으로 넣어준다.

-------------------

## webpack

- 웹펙은 현재 가장 널리 쓰이는 번들러.
- JS뿐만 아니라, CSS, IMAGE 파일 등 리소스의 의존성들도 관리한다.

### 모듈

- 어플리케이션을 구성하는 개별적 요소
- 재사용 가능한 코드 조각
- 모듈은 세부사항을 캡슐화한다.
- 특정 기능을 갖는 작은 코드 단위

### 모듈 번들러

- 웹 어플리케이션을 구성하는 자원(HTML, CSS, JS, IMG 등)을 모두 각각의 모듈로 보고 이를 조합해서 병합된 하나의 결과물로 만드는 도구

---------------

개발을 편하게 모듈 단위 개발 => 모듈끼리 연결(의존성)을 신경쓰기가 어려워짐 => 웹팩아 하나로 만들어줘.

### entry

- 여러 js 파일들의 시작점 -> 웹팩이 파일을 읽어 들이기 시작하는 부분

### module

- 웹팩은 JS만 변환 가능하기 때문에 html, css 등은 모듈을 통해서 웹팩이 이해할 수 있도록 변환이 필요하다.
- 변환 내용을 담는 곳.

### plugins

- 웹팩을 통해서 번들된 결과물을 추가 처리하는 부분.

### output

- 여러 js 파일을 **하나로 만들어 낸 결과물**

---------

- vue 웹팩 설치(-D : 개발자 모드)

> $ npm init
>
> $ npm install vue
>
> $ npm i webpack webpack-cli -D

- 웹팩은 js 코드만 이해 가능하기 때문에 vue파일(vue-loader) 및 html, css 파일(vue-template-compiler) 등을 변환하기 위하여 모듈을 설치

> $ npm install vue-loader vue-template-compiler -D
>
> $ npm install vue-style-loader css-loader -D

- ### 모든 과정을 한번에 만들어줌

> $ npm i -g @vue/cli

----------------

최상위 컴포넌트(App.vue)

하위 컴포넌트(TodoList.vue)

---------

### 컴포넌트 등록 3 steps (App.vue)

1. `<script>` 에 등록할 컴포넌트 불러오기 (import)
2. `export default`에 `components` 항목 추가
3. `<template>` 에서 컴포넌트 사용할 수 있도록 등록

--------------

- 웹팩을 직접 작성했을 때 만들었던 `webpack.config.js` 가 보이지 않는다.
- `vue.config.js` 는 vue-cli 에 의해 자동으로 로드되는 선택적 구성파일로 변경되었다.
- vue-cli 3 버전부터 노출되지 않으며, 설정을 추가하기 위해서는 루트 디렉토리에 직접 파일을 만들고 작성해야 한다.