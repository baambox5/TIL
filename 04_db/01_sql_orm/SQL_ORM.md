[TOC]

# SQL과 django ORM

## 기본 준비 사항

```bash
# 폴더구조

TIL
	00_StartCamp
	...
	04_db
		00_sql # only SQL
			hellodb.csv
			tutorial.sqlite3
			users.csv
		01_sql_orm # SQL + ORM
			...
			users.csv # 해당 디렉토리로 다운로드
```

* django app

  * 가상환경 세팅

  * django project : `sql`

  * django app : `users`

  * `django_extensions` 설치 및 등록

  * users.csv 파일에 맞춰 `models.py` 작성 및 migratation

    ```python
    # users/models.py
    
    from django.db import models
    
    class User(models.Model):
        first_name = models.CharField(max_length=10)
        last_name = models.CharField(max_length=10)
        age = models.IntegerField()
        country = models.CharField(max_length=10)
        phone = models.CharField(max_length=15)
        balance = models.IntegerField()
    ```

    ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate 
    ```

    아래의 명령어를 통해서 실제 쿼리문 확인

    ```bash
    $ python manage.py sqlmigrate users 0001
    ```

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ ls
    db.sqlite3 manage.py ...
    $ sqlite3 db.sqlite3
    ```

  * csv 파일 data 로드

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    sqlite > SELECT COUNT(*) FROM users_user;
    100
    ```

* 확인

  * sqlite3에서 스키마 확인

    ```sqlite
    sqlite > .schema users_user
    CREATE TABLE IF NOT EXISTS "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(10) NOT NULL, "last_name" varchar(10) NOT NULL, "age" integer NOT NULL, "country" varchar(10) NOT NULL, "phone" varchar(15) NOT NULL, "balance" integer NOT NULL);
    ```



---



## 문제

> 아래의 문제들을 보면서 서로 대응되는 ORM문과 SQL문을 작성하시오.
>
> **vscode 터미널을 좌/우로 나누어 진행하시오. (sqlite / shell_plus)**

`.headers on` 을 켜고 작성해주세요.



### 1. 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   >>> User.objects.all().values()
   ```

      ```sql
   -- sql
   sqlite> SELECT * FROM users_user
      ```

2. user 레코드 생성

   ```python
   # orm
   >>> user = User()
   >>> user.first_name = '민정'
   >>> user.last_name = '김'
   >>> user.age = 25
   >>> user.country = '부산광역시'
   >>> user.phone = '011-2145-2125'
   >>> user.balance = 3800
   >>> user.save()
   ```

   ```sql
   -- sql
   INSERT INTO users_user
      ...> (first_name, last_name, age, country, phone, balance)
      ...> VALUES ('민희', '강', 22, '경기도', '010-3245-2152', 20);
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

     * sqlite3.IntegrityError: NOT NULL constraint failed: users_user.balance

       django.db.utils.IntegrityError: NOT NULL constraint failed:
       users_user.balance

     * Error: NOT NULL constraint failed: users_user.balance

3. 해당 user 레코드 조회

   - `101` 번 id의 전체 레코드 조회

   ```python
   # orm
   >>> User.objects.filter(pk=101).values()
   ```

   ```sql
   -- sql
   sqlite> SELECT * FROM users_user WHERE id=101;
   ```

4. 해당 user 레코드 수정

   - ORM: `101` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `101` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   >>> user = User.objects.get(pk=101)
   >>> user.last_name = '김'
   >>> user.save()
   ```

      ```sql
   -- sql
   sqlite> UPDATE users_user SET first_name='철수' WHERE id=101;
      ```

5. 해당 user 레코드 삭제

   - ORM: `101` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 (ORM에서 삭제가 되었기 때문에 아무런 응답이 없음)

   ```python
   # orm
   >>> user = User.objects.get(pk=101)
   >>> user.delete()
   ```
   
   ```sql
   -- sql
      sqlite> DELETE FROM users_user WHERE id=101;
   ```
   
   

---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
   >>> User.objects.all().count()
   100
   ```

   ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user;
   COUNT(*)
   100
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   >>> User.objects.filter(age=30).values('first_name')
   <QuerySet [{'first_name': '영환'}, {'first_name': '보람'}, {'first_name': '은영'}]>
   ```

      ```sql
   -- sql
   sqlite> SELECT first_name FROM users_user WHERE age=30;
   first_name
   "영환"
   "보람"
   "은영"
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   ```python
   # orm
   >>> User.objects.filter(age__gte=30).count()
   43
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age>=30;
   COUNT(*)
   43
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   >>> User.objects.filter(age__lte=20).count()
   23
   ```

   ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user WHERE age<=20;
   COUNT(*)
   23
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   >>> User.objects.filter(age=30, last_name='김').count()
   1
   ```

      ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user WHERE age=30 and last_name='김';
   COUNT(*)
   1
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   # orm
   >>> User.objects.filter(age=30).values() | User.objects.filter(last_name='김').values()
   
   >>> User.objects.filter(Q(age=30)|Q(last_name='김')).values()
   ```

   ```sql
   -- sql
   sqlite> SELECT * FROM users_user WHERE age=30 or last_name='김';
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   >>> User.objects.filter(phone__startswith='02-').count()
   24
   ```

      ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user WHERE phone LIKE '02-%';
   COUNT(*)
   24
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   >>> User.objects.filter(country='강원도').values('first_name') & User.objects.filter(last_name='황').values('first_name')
<QuerySet [{'first_name': '은정'}]>
   
   # 은정까지 들어가기
   >>> User.objects.filter(country='강원도', last_name='황').values('first_name').first().get('first_name')
   ```
   
      ```sql
   -- sql
   sqlite> SELECT first_name FROM users_user WHERE country='강원도' and last_name='황';
   first_name
   "은정"
      ```



---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

   ```python
   # orm
   >>> User.objects.order_by('-age')[:10].values()
   ```

      ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY age DESC LIMIT 10;
   id|first_name|last_name|age|country|phone|balance
   1|정호|유|40|전라북도|016-7280-2855|370
   4|미경|장|40|충청남도|011-9079-4419|250000
   28|성현|박|40|경상남도|011-2884-6546|580000
   53|상훈|홍|40|전라북도|016-7698-6684|550
   65|민서|송|40|경기도|011-9812-5681|51000
   26|영식|이|39|경상북도|016-2645-6128|400000
   55|미경|이|39|경기도|02-6697-3997|890000
   58|영일|배|39|전라남도|010-3486-8085|280000
   74|승민|배|39|강원도|010-4833-9657|840
   82|현지|김|39|충청북도|02-8468-8321|680000
      ```

2. 잔액이 적은 사람순으로 10명

   ```python
   # orm
   >>> User.objects.order_by('balance')[:10].values()
   ```

      ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY balance LIMIT 10;
   id|first_name|last_name|age|country|phone|balance
   99|우진|성|32|전라북도|010-7636-4368|150
   48|보람|이|28|강원도|02-2055-4138|210
   100|재현|김|25|경상북도|016-1252-2316|210
   5|영환|차|30|충청북도|011-2921-4284|220
   24|숙자|권|33|경상남도|016-4610-3200|230
   61|우진|고|15|경상북도|011-3124-1126|300
   92|미경|박|35|경상북도|010-5203-5705|300
   46|명자|김|23|전라남도|011-3545-5608|330
   38|준호|심|28|충청북도|016-6703-7656|340
   60|은영|김|30|경상북도|02-5110-2334|350
      ```

3. 잔고는 오름차순, 나이는 내림차순으로 10명?

      ```python
   # orm
   >>> User.objects.order_by('balance', '-age')[:10].values()
```
   
   ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY
      ...> balance, age DESC LIMIT 10;
   ```
   
4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   >>> User.objects.order_by('-last_name', '-first_name')[4]
```
   
      ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY last_name DESC, first_name DE
   SC LIMIT 1 OFFSET 4;
      ```



---



### 4. 표현식

> ORM: `aggregate` 사용
>
> https://docs.djangoproject.com/en/2.2/topics/db/aggregation/#aggregation
>
> - '종합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용

1. 전체 평균 나이

   ```python
   # orm
   >>> User.objects.aggregate(average_value=Avg('age'))
   {'average_value': 28.23}
   ```

      ```sql
   -- sql
   sqlite> SELECT AVG(age) FROM users_user;
   AVG(age)
   28.23
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   >>> User.objects.filter(last_name='김').aggregate(Avg('age'))
   {'age__avg': 28.782608695652176}
   ```

      ```sql
   -- sql
   sqlite> SELECT AVG(age) FROM users_user WHERE last_name='김';
   AVG(age)
   28.7826086956522
      ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   >>> User.objects.filter(country='강원도').aggregate(average_value=Avg('balance'))
   {'average_value': 157895.0}
   ```

   ```sql
   -- sql
   sqlite> SELECT AVG(balance) FROM users_user WHERE country='강원도';
   AVG(balance)
   157895.0
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   >>> User.objects.aggregate(Max('balance'))
   {'balance__max': 1000000}
   ```

      ```sql
   -- sql
   sqlite> SELECT MAX(balance) FROM users_user;
   MAX(balance)
   1000000
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   >>> User.objects.aggregate(Sum('balance'))
{'balance__sum': 14425040}
   ```
   
      ```sql
   -- sql
   sqlite> SELECT SUM(balance) FROM users_user;
   SUM(balance)
   14425040
      ```