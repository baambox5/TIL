## JS 함수는 일급객체

1. 변수에 담을 수 있다.
2. 인자로 전달할 수 있다.
3. 반환값으로 전달할 수 있다.

-----------------

### 비동기식 처리 모델

- 호출될 함수 (콜백함수)를 미리 매개변수에 전달하고 처리가 종료되면, 콜백함수를 호출하는 것.

-------------------

### 이벤트 리스너

`EventTarget.addEvenListener(type, listener)`

1. 무엇을 (버튼을)
2. 언제 (클릭했을 때)
3. 어떻게 (콘솔에 로그를)



- vue에서 this를 사용시 다른 것을 가리키게 되므로, 화살표 함수가 아닌 **일반 표현식**으로 사용

------------------

### JS 코드를 body의 최하단에 위치하는 이유

1. JS를 읽는 시간때문에 BODY 안에 있는 HTML 요소들이 브라우저에 그려지는게 지연될 수 있기 때문.
2. JS에서 특정 HTML 요소들을 읽고 이벤트를 등록해야 할 때, JS 코드가 먼저 해석되면 해당 요소가 없다고 인식되어 이벤트 등록이 되지 않을 수 있기 때문.

---------------

querySelector는 위에서 선택자로 요소를 찾으며 가장 먼저 찾아지는 요소를 반환(단수)

querySelectorAll은 위에서부터 선택자로 요소를 찾으며 일치하는 요소들을 모두 반환(복수)

--------------------------

## 동기식 처리 모델

- 직렬적으로 task를 수행
- 태스크는 순차적으로 실행되며 어떤 작업이 수행중이면 다음 작업은 대기
- 예) 서버에서 데이터를 가져와서 화면에 표시하는 작업을 수행할 때, 데이터가 응답될 때까지 이후 태스크들은 블로킹(blocking)된다.

## 비동기식 처리 모델(Asynchronous)

- 병렬적으로 태스크를 수행
- 태스크가 종료되지 않는 상태라 하더라도 대기하지 않고 다음 태스크를 실행
- 예) 서버에서 데이터를 가져와서 화면에 표시하는 작업을 수행할 때, 데이터가 응답될 때까지 기다리지 않고(non-blocking) 즉시 다음 태스크를 수행.
- JS 대부분의 DOM 이벤트와 Timer 함수, Ajax 요청은 비동기식 처리 모델로 동작.

----------------------------------

## blocking vs non-blocking

### 이벤트 루프

- 단 한가지 **콜스택**과 **콜백큐**를 감시하는 역할만 합니다.
- 만약 콜스택이 비어 있으면 이벤트 루프는 콜백큐에서 첫 번째 이벤트를 가져다가 콜스택에 밀어 넣고, 결과적으로 해당 이벤트가 실행된다.
- 이러한 반복은 이벤트 루프에서는 `tick`이라고 한다.
- 이벤트루프는 호스팅 환경(브라우저 or nodejs)에 내장된 메커니즘 (JS 엔진에 있는게 아니다)
- 이것은 시간의 흐름에 따라 코드의 수행을 처리하며 그때마다 JS엔진을 작동시킨다.

### setTimeout(mycallback, msecs)

- callback 함수가 1초뒤에 실행될 것이다라는 의미가 아니다.
- 만약에 콜백 큐에 mycallback보다 먼저 추가된 이벤트가 있을 수도 있기 때문에 실제 1초보다 더 오랜시간이 걸릴 수도 있다.

---------------------

## Axios

- `axiosXHR`을 요청으로 보내고 응답 받은 결과를 `Promise 객체`로 반환해주는 라이브러리
- axios는 현재 JS에서 가장 HOT한 라이브러리 중 하나이며 프론트엔드 프레임워크(react, vue)에서 데이터를 주고 받을 때 필수적으로 사용되고 있음 (프론트엔드 프레임워크 <-> api 서버)