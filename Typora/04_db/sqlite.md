## Database

##### RDBMS

- 관계형 데이터베이스 관리 시스템
- 테이블 형식(지금까지 해왔던 것)

##### schema

- 데이터베이스의 구조와 제약 조건(자료의 구조, 표현 방법, 관계)에 관련한 전반적인 명세를 기술한 것.



- 빈 데이터 베이스 만들기

> $ sqlite3 {데이터베이스 파일 이름}.sqlite3
>
> sqlite> .databases

- mode 바꾸기

> sqlite> .mode csv

- import하기

> sqlite> .import hellodb.csv {테이블 이름}

- 조회

> sqlite> SELECT * FROM {테이블 이름};

- 보이는 것 바꾸기

> sqlite> .headers on
> sqlite> .mode column
> sqlite> SELECT * FROM examples;
>
> id          first_name  last_name   age         country     phone
>
> ----------  ----------  ----------  ----------  ----------  -------------
> 1           길동          홍           600         충청도         010-2424-1232

- 테이블 만들기

> sqlite> CREATE TABLE classmates (
>    ...> id INTEGER PRIMARY KEY,
>    ...> name TEXT
>    ...> );



`.` : sqlite3 프로그램의 기능을 실행하는 것.

`;` : 세미콜론까지가 하나의 명령(Query)으로 간주

- SQL 문법은 소문자로 작성해도 된다. (단, 대문자를 권장)
- 하나의 DB에는 여러 개의 table이 존재한다.
- 모든 열에 데이터를 넣을 때에는 column명을 명시할 필요가 없다. (INSERT 사용시에)
- 꼭 필요한 데이터 항목이라면 빈 값이 있어서는 안된다. (데이터 무결성 원칙)
- Primary key는 직접 만들면, 모든 요소의 데이터를 넣을 때(INSERT) 요소명 생략이 안된다. id값도 넣어야하기 때문. (가능하면 rowid를 사용하자!, AUTOINCREMENT를 쓸때가 있을 수도 있다. - 그러나 내부적으로 CPU, 메모리 상의 낭비로 인해, 사용을 권장하지 않음.)
  - INSERT INTO를 한다면
    1. AUTOINCREMENT가 없을 때: 중간에 없는 ID를 재사용하므로 에러가 발생하지 않음.
    2. AUTOINCREMENT가 있을 때: 범위를 벗어나므로 에러가 발생할 가능성.



> # 한 개의 데이터를 3번째 것을 가져오기
>
> sqlite> SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
> rowid       name
>
> ----------  ----------
> 3           박나래

> # 주소가 서울인 것만 가져오기
>
> sqlite> SELECT rowid, name FROM classmates WHERE address='서울';
> rowid       name
>
> ----------  ----------
> 1           홍길동

> # 해당되는 내용 중복 없이 가져오기
>
> sqlite> SELECT DISTINCT age FROM classmates;
>
> age
>
> --------
>
> 30
> 23
> 33

> # 해당되는 id를 지운다.
>
> sqlite> DELETE FROM classmates WHERE rowid=3;
> sqlite> SELECT rowid, * FROM classmates;
> rowid       name        age         address
>
> ----------  ----------  ----------  ----------
> 1           홍길동         30          서울
> 2           김철수         23          대전
> 4           최철순         45          서울

> # 데이터 내용 바꾸기
>
> sqlite> UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=4;
> sqlite> SELECT * FROM classmates
>    ...> ;
> name        age         address
>
> ----------  ----------  ----------
> 홍길동         30          서울
> 김철수         23          대전
> 홍길동         45          제주도
> 박나래         23          광주

##### LIKE

- `%` : 있을수도 있고, 없을수도 있다.
- `_` : 반드시 있어야한다.

> # LIKE 활용 (중간번호가 5114인 것을 찾기)
>
> sqlite> SELECT * FROM users WHERE phone LIKE '%-5114-%';
> id,first_name,last_name,age,country,phone,balance
> 240,"현준","황",37,"충청북도",011-5114-9343,220

##### order

- 정렬하기

> # 나이 순으로 내림차순 정렬하여 상위 10개만 뽑기
>
> sqlite> SELECT * FROM users ORDER BY age DESC LIMIT 10;

##### alter

1. 테이블 이름 변경

> sqlite> ALTER TABLE articles RENAME TO news;

2. 새로운 컬럼 추가

> sqlite> ALTER TABLE news ADD COLUMN created_at DATETIME NOT NULL;
> Error: Cannot add a NOT NULL column with default value NULL
>
> 이 경우에 NOT NULL 조건을 없애거나, 기본값(DEFAULT)를 지정해야 함.
>
> 1) sqlite> ALTER TABLE news ADD COLUMN created_at DATETIME;
>
> 2) sqlite> ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT 1;

