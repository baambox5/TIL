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