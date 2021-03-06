# JavaScript_intro

### let (변수)

- 값을 재할당 할 수 있는 변수를 선언.
- 단, 각 변수는 **한번만 선언**할 수 있다. (할당은 여러번 가능) 
- 블록 유효 범위(block scope)



### const (상수)

- 값이 변하지 않는 상수를 선언하는 키워드
- 담긴 값이 불변임을 뜻하는 게 아니다.
- 단지 상수의 값은 재할당 할 수 없고, 재선언도 안된다.
- 블록 유효 범위(block scope)



### var (변수)

- ES6 이전의 feature로 예기치 않은 문제를 많이 발생시키는 키워드로 **절대 사용하지 않는다**.
- 함수 유효 범위(function scope)
- var로 선언된 변수의 범위는 현재 실행 문맥인데, 그 문맥이 함수 혹은 함수 외부의 전역으로도 갈 수 있다.



------------------

- var를 제외하고 어떤 변수를 쓸지 결정하는 건 프로그래머의 몫.
- `PI`, `DAYS_IN_JUNE`과 같은 경우는 상수가 적절
- `WEATHER_TEMP`처럼 모호한 경우(각자가 생각하는 좋아하는 기온이 다를 수 있으니까) 이런 경우는 변수가 적절

-------------------

- 일단 모든 선언에서 가능한한 상수를 사용해야 한다.
- 먼저, 상수를 생각하고 값이 바뀌는 것이 더 자연스러운 상황이라면, 그때 변수로 바꿔서 사용하는 것을 권장.

-----------------

- var : 할당 및 선언 자유 / 함수 스코프
- let : 할당 자유 / 선언은 한번만 / 블록 스코프
- const : 할당 및 선언 모두 한번만 / 블록 스코프

----------------

## 식별자(identifier)

- 변수명은 식별자라고 불리며 특정 규칙을 따른다.

1. 반드시 문자, 달러($), 또는 밑줄로 시작해야 한다. 이후는 숫자도 가능.
2. 대소문자를 구분하며 클래스명을 제외하고는 대문자로 시작하지 않는 것이 좋다.
3. 예약어는 사용 불가능(class, super, const, case, function ...)



------------------------

## hoisting

- 이 개념은 JS 변수, 함수나 표현이 최상단으로 올려지는 것을 말한다.
- 끌어 올려진 변수는 `undefined` 값을 반환한다.
- 변수와 함수를 위한 메모리 공간을 확보하는 과정.



---------------------------

### var 할당과정

1. 선언 + 초기화
2. 할당

### let 할당과정

1. 선언
2. TDZ(Temporal Dead Zone, 임시적 사각지대) - block단위의 어떤 공간
3. 초기화
4. 할당

--------------------

let, const의 정의가 평가되기까지 초기화가 되지 않는다는 의미이지, 호이스팅이 되지않아 정의가 되지 않는다는 의미와는 다르다.

-------

Babel 로 ES6+ 문법을 그보다 아래 버전의 JS로 변경해서 사용하기도 한다.

-----------------------

## 타입과 연산자

### 타입

1. Primitive
2. Reference



- #### Primitive

  - 불변하다는 특징을 띄고 있다.

  1. Numbers

     - `Infinity` : 양의 무한대와 음의 무한대로 나뉨
     - `NaN` : Not a Number, 표현할 수 없는 값, 자기 자신과 일치하지 않는 유일한 값을 표현
       - 0/0, "문자" * 10, Math.sqrt(-9)

  2. Strings

     - `Literal`

       - 값을 프로그램 안에서 직접 지정한다는 의미
       - 값을 만드는 방법
       - JS는 우리가 제공한 리터럴 값을 받아 데이터를 만듦

       ```javascript
       // room 변수를 가리키는 식별자 / 'conference_room'(따옴표 안)은 리터럴
       let room = 'conference_room'
       
       let hotelRoom = room
       
       // 에러, conference_room 식별자는 존재하지 않는다.
       hotelRoom = conference_room
       ```

       - JS는 따옴표를 통해 리터럴과 식별자를 구분한다.
       - 식별자는 숫자로 시작할 수 없으므로, 숫자에는 따옴표가 필요없다. (숫자형 리터럴)

  3. Boolean

  4. Empty Value

     - `null // undefined`

       - 동일한 역할을 하는 이 2개의 키워드가 존재하는 이유는 단순한 JS의 설계 실수
       - 큰 차이를 두지 말고, interchangeable하게 사용할 수 있도록 권장.

       `undefined`

       - 값이 없을 경우 JS가 자동으로 할당해주는 값

         ```javascript
         let first_name // 선언만 하고 할당하지 않음.
         console.log(first_name)	// undefined
         ```

       `null`

       - 값이 없음을 우리가 표현하기 위해서 인위적으로 사용하는 값

         ```javascript
         let last_name = null
         console.log(last_name) // null - 의도적으로 값이 없음을 표현
         ```



## 연산자

- 'A' < 'B'

  > true

- 'Z' < 'a'

  > true

- const a = 1

  > undefined

  const b = '1'

  > undefined

  a == b

  > true

  a === b

  > false

  a === Number(b)

  > true

- 8 * null

  > 0

- '5' - 1

  > 4

- '5' + 1

  > "51"

- !true

  > false

- true ? 1 : 2 (콜론을 기준으로 물음표 앞의 boolean값이 참이면 1번 위치의 식을 실행)

  > 1

  false ? 1 : 2 (콜론을 기준으로 물음표 앞의 boolean값이 거짓이면 2번 위치의 식을 실행)

  > 2

  const result = Math.PI > 4 ? 'yes' : 'no'

  > undefined

  result

  > "no"

- const userName = prompt('Hello! who r u??')

  > undefined

  userName

  > "harry"

- document.write(message)

  > undefined



# Datastructure : Object와 Array

## JSON(JS Object Notation, JS 객체 표기법)

- KEY-VALUE 형태의 자료구조를 JS 객체와 유사한 모습으로 표현하는 표기법
- 모습만 비슷할 뿐이고 실제로 Object처럼 사용하려면 다른 언어들처럼 JS에서도 Parsing(구문 분석) 작업이 필요하다.

### 정리

- Object : JS의 key-value 페어의 자료 구조
- JSON : 데이터를 표현하기 위한 **단순한 문자열**, 트레일링 콤마는 사용 불가

------------------

## Helper Method

- Helper란 자주 사용하는 로직을 재활용할 수 있게 만든 일종의 Library다.

---------------------

### callback

- 인수로 다른 함수에 전달된 함수
- 명시적으로 호출하는 방식이 아니라 **특정 이벤트가 발생했을 때** 시스템에 의해 호출되는 함수
  - 다른 함수의 실행이 끝나고 난 뒤에 실행되는 함수. 이따가 너 실행 끝나면 그때 나 좀 호출해줘.
- 함수 호출권한을 내가 아닌 시스템이 가진다.