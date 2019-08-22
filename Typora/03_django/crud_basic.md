# CRUD

- Create(만들고), Read(읽고), Update(수정하고), Delete(지운다)

- ORM : SQL과 python code 사이에서 처리

  - 장점

    1. SQL을 몰라도 사용할 수 있다.
    2. SQL의 절차적인 접근이 아닌 객체 지향적 접근 가능
    3. 매핑 정보가 명확하여, ERD(모델간의 관계 diagram(table))를 보는 것에 대한 의존도를 낮출 수 있다.
    4. ORM은 독립적으로 작성되어 있고, 해당 객체들을 재활용할 수 있다. 개발자는 객체에 집중함으로써, 해당 DB에 종속될 필요없이 자유롭게 개발할 수 있다.

  - 단점

    1. ORM만으로 완전히 거대한 서비스를 구현하기가 어렵다.

       - 사용하기는 편하지만, 설계는 매우 신중하게 해야함.

       - 프로젝트의 규모가 커질 경우, 난이도가 올라가게 된다.

       - 순수 SQL보다 약간의 속도 저하가 생길 수 있다.

    2. 이미 프로세스가 많은 시스템에서는 ORM으로 대체하기가 어렵다.

- 단점들이 있음에도 사용하는 이유는 **생산성**! ORM을 사용하여 얻게되는 생산성은 약간의 성능저하나 다른 단점들을 상쇄할 만큼 뛰어나기 때문.

- 장점으로 인한 생산성 증가가 훨씬 크기 때문에, 현대에는 대부분의 프레임워크들이 ORM을 사용하고 있다.

- 즉, 우리는 DB를 객체(object) - 인스턴스(instance)로 조작하기 위해 ORM을 배운다.



## 모델의 개념

- 모델은 단일한 데이터에 대한 정보를 가지고 있다.
- 필수적인 필드(컬럼, 열)와 데이터(레코드, 행)에 대한 정보를 포함한다. 일반적으로 각각의 **모델(클래스)**는 단일한 데이터베이스 **테이블과 매칭(연결, 연동)**된다.
- 모델은 부가적인 메타데이터를 가진 **DB의 구조(layout)**를 의미
- 사용자가 저장하는 데이터들의 **필수적인 필드와 동작(behavior)**을 포함



공식문서 : https://docs.djangoproject.com/en/2.2/ref/models/fields/

### CharField()

- 길이의 제한이 있는 문자열을 넣을 때 사용
- `max_length`는 필수 인자다.
- 필드의 최대 길이(문자)이며 DB와 django의 유효성검사(값을 검증)에서 사용됨.
- 텍스트 양이 많을 경우 `TextField()`로 사용



### TextField()

- 글의 수가 많을 때 사용
- max_length 옵션을 줄 수 있지만, 모델과 실제 DB에는 적용되지 않는다. 길이 제한을 주고 싶다면, CharField()를 사용해야 한다.



### DateTimeField()

- 시간과 날짜를 기록하기 위한 필드
- `auto_now_add=True`
  - django ORM이 최초 INSERT(테이블에 데이터 입력)시에만 현재 날짜와 시간 작성
  - **최초 생성 일자**
- `auto_now=True`
  - django ORM이 SAVE를 할 때마다 현재 날짜와 시간 작성
  - **최종 수정 일자**



## model 로직

- DB 컬럼과 어떠한 타입으로 정의할 것인지에 대해 `django.db`모듈의 `models`의 상속을 받아서 적용된다.
- 각 모델은 **`django.db.models.Model`클래스의 서브 클래스**로 표현된다. (자식클래스)
- 모든 필드는 기본적으로(자동) NOT NULL 조건이 붙는다. (NULL 값이 들어갈 수 없다.)
- 각각의 **클래스 변수**들은 **모델의 데이터베이스 필드**를 나타낸다.



### Migrations

1. `migrations`
   - makemigrations 명령어는 모델(model.py)을 작성/변경한 사항을 django에게 알리는 작업. (ORM에 보낼 PYTHON 코드 설계도를 작성)
   - 테이블에 대한 설계도(django ORM이 만들어줌)를 생성.
2.  `migrate`
   - migrations로 만든 설계도를 기반으로 실제 `db.sqlite3` DB에 반영한다.(테이블을 만듦)
   - **모델에서의 변경사항들과 DB 스키마가 동기화를 이룬다.**



- **migrations 하기(설계도 생성)**

> $ python manage.py makemigrations

- 해당 migrations 설계도가 SQL문으로 어떻게 해석되어서 동작할 지 확인방법((ex) articles의 0001_initial)

> $ python manage.py sqlmigrate articles 0001
>
> $ python manage.py sqlmigrate <app_name> <file_name앞 숫자> 

- migrations 설계도들이 migrate 됐는지 안됐는지 확인

> $ python manage.py showmigrations

- migrate하기

> $ python manage.py migrate



- vs code에서 sqlite보기

  >  vs code에 sqlite라는 extension설치 => F1 => sqlite검색 => open database



### Model 변경 시 작성 순서

1. `models.py` : 작성 및 변경(생성 / 수정)
2. `makemigrations` : migrations 파일 만들기(설계도)
3. `migrate` : 실제 DB에 적용 및 동기화(테이블 생성)

- 테이블의 이름은 app 이름과 model에 작성한 class 이름이 조합되어져서 자동으로 만들어진다(**모두 소문자**).



- sqlite3 설치방법

  > sqlite3 검색 => 다운로드 항목 => **Precompiled Binaries for Windows**의 두번째, 세번째 다운로드 => c드라이브에 sqlite폴더 생성 => 안쪽에서 다운받은 압축파일들 현재 폴더에 압축 풀기 => 안에 폴더들 없게 다 C:\sqlite로 빼내기 => 환경변수 => 시스템변수 => path => 새로만들기 => C:\sqlite추가

- sqlite 실행방법

  > $ winpty sqlite3

- alias등록

  > code .bashrc에 alias sqlite3="winpty sqlite3" 추가
  >
  > $ source ~/.bashrc

- **등록 후 sqlite 실행방법**

  > $ sqlite3 <file_name>

- **sqlite 종료**

  > $ .exit



- 테이블 확인

  > sqlite> .tables

- sql 코드 확인

  > sqlite> .schema articles_article



## CRUD (DB API 조작)

1. Django Shell
   - django 프로젝트 설정이 로딩된 파이썬 shell
   - 일반 파이썬 shell로는 django 환경에 접근 불가
   - 즉, django 프로젝트 환경에서 파이썬 shell을 활용한다고 생각



- shell 관련 추가 설치(컬러링으로 좀 더 보기 편함)

  > $ pip install ipython



## Create

### QuerySet 기본 개념

- 전달 받은 객체의 목록
  - QuerySet : 쿼리 set 객체
  - Query : 단일 객체
- DB로부터 데이터를 읽고, 필터를 걸거나 정렬 등을 수행
- Query를 던지는 Language를 활용해서 DB에게 데이터에 대한 조작을 요구한다.

#### `QuerySet`

- objects를 사용하여 다수의 데이터를 가져오는 함수를 사용할 때, 반환되는 객체
- 단일한 객체를 반환(리턴)할 때는 테이블(class)의 인스턴스로 리턴됨.

#### `objects`

- Model Manager와 Django Model 사이의 Query 연산의 인터페이스 역할을 해주는 친구
- 즉, `models.py`에 설정한 클래스(테이블)을 불러와서 사용할 때, DB와의 인터페이스 역할(쿼리를 날려주는)을 하는 매니저이다.
- 쉽게 이해하려면 ORM의 역할이라고 생각하면 된다.
- DB ---------- objects ----------- Python Class(models.py)
- manager(objects)를 통해 특정 **데이터를 조작(메서드)**할 수 있다.



데이터 객체를 만드는(생성, CREATE)하는 3가지 방법 (보통 첫번째 방법을 사용한다.)

1. 첫번째 방법

   ```python
   $ python manage.py shell
   
   # SQL - 특정 테이블에 새로운 레코드(행)을 추가하여 데이터 추가
   # INSERT INTO table (column1, column2, ...) VALUES (value1, value2, ...)
   # INSERT INTO articles_article (title, content) VALUES ('first', 'django!')
   
   >>> aricle = Article()	# Article class로부터 article 인스턴스 생성
   >>> article.title = 'first'	# article 인스턴스의 title 변수에 값 할당
   >>> article.content = 'django!'	# 인스턴스 변수(content)에 값을 할당
   
   # save를 하지 않으면 아직 DB에 값이 저장되지 않음
   >>> article
   <Article: Article object (None)>
   >>> Article.objects.all()
   <QuerySet []>
   
   # save를 하고 확인해보면 저장된 것을 확인할 수 있다.
   >>> article.save()
   >>> article
   <Article: Article object (1)>
   >>> Article.objects.all()
   <QuerySet [<Article: Article object (1)>]>
   
   # 인스턴스 article을 활용하여 변수에 접근할 수 있다(저장된 값 확인)
   >>> article.title
   'first'
   >>> article.content
   'django!'
   >>> article.created_at
   datetime.datetime(2019, 8, 21, 2, 43, 56, 782386, tzinfo=<UTC>)
   ```

   

2. 두번째 방법

   ```python
   >>> article = Article(title='second', content='django!!')
   >>> article.save()
   ```

   

3. 세번째 방법

   - `create()`를 사용하면 쿼리셋 객체를 생성하고 저장하는 로직이 한 번의 스텝으로 끝난다.

   ```python
   >>> Article.objects.create(title='third', content='django!!!')
   ```



- 유효성 검사
  - save 전에 `full_clean()`메서드를 통해 article이라는 인스턴스 객체가 검증(validation)에 적합한지를 알아 볼 수 있다.
  - `models.py`에 필드 속성과 옵션에 따라 검증을 진행한다.
  - 세번째 방법인 `create()`를 사용할 경우에는 유효성 검사를 할 기회도 없이 진행해버린다.

```python
>>> article.full_clean()
```



- model 수정시 해야할 것.
  - 간단한 것은 왠만하면 django가 처리해주지만(그래도 위쪽의 순서를 따를 것), 안 되면 0001~ 숫자 붙은 것 지우고, db.sqlite3도 지우고 위쪽의 Model 변경 시 작성 순서를 따를 것.



## READ

### Article.objects.all()

- 테이블 내용을 전부 조회(READ)
- DB에 쿼리를 날려서 인스턴스 객체 전부를 달라고 하는 뜻
- 만약에 레코드가 하나라면, 인스턴스 단일 객체로 반환
- 두개 이상이면, QuerySet 형태로 반환
- SELECT * FROM articles_article; 과 동일한 동작



- READ

  ```python
  # 1. SELECT * FROM articles_article;
  # 1. DB에 있는 모든 글 가져오기
  >>> Article.objects.all()
  
  # 2. SELECT * FROM articles_article WHERE title='first';
  # 2. DB에 저장된 글 중에서 title이 first인 글만 가져오기
  >>> Article.objects.filter(title='first')
  
  # 3. SELECT * FROM articles_article WHERE title='first' LIMIT 1;
  # 3. DB에 저장된 글 중에서 title이 first인 글 중에서 첫번째 글만 가져오기
  >>> Article.objects.all().first()
  >>> Article.objects.all().last()	# 마지막 값
  
  # 4-1. SELECT * FROM articles_article WHERE id=1;
  # 4-1. DB에 저장된 글 중에서 PK가 1인 글만 가져오기
  >>> Article.objects.get(pk=1)
  # PK만 .get()으로 가져올 수 있다. (.get()은 값이 중복이거나 일치하는 값이 없으면 에러를 발생시킨다.) 즉, pk에만 사용하자.
  
  # 4-2. filter의 경우 존재하지 않으면 에러가 아닌 빈 쿼리셋을 반환한다. 마치 딕셔너리에서 value를 꺼낼 때 [] 방식으로 꺼내는지 혹은 .get 으로 꺼내는지의 차이와 유사하다.
  >>> Article.objects.filter(pk=100)
  <QuerySet []>
  
  # 4-3. filter / get
  # filter 자체가 여러 값을 가져올 수 있기 때문에, django가 개수를 보장하지 못한다. 그래서 0개, 1개라도 무조건 쿼리셋으로 반환한다.
  
  # 5-1. 오름차순
  # SELECT * FROM articles_article ORDER BY title ASC;
  >>> Article.objects.order_by('pk')
  
  # 5-2. 내림차순
  # SELECT * FROM articles_article ORDER BY title DESC;
  >>> Article.objects.order_by('-pk')
  
  # 6. 쿼리셋은 LIST 자료형은 아니지만, LIST에서 할 수 있는 인덱스 접근 및 슬라이싱이 모두 가능하다.
  >>> Article.objects.all()[2]
  >>> Article.objects.all()[1:3]
  
  # 7. LIKE / starswith /endswith
  # django ORM은 이름(title)과 필터(contains)를 더블언더스코어(__)로 구분한다.
  # 더블언더스코어 == 던더(dunder)스코어
  
  # LIKE
  >>> Article.objects.filter(title__contains='fir')
  
  # startswith
  >>> Article.objects.filter(title__startswith='fir')
  
  # endswith
  >>> Article.objects.filter(content__endswith='!')
  ```

  

## UPDATE

```python
# article 인스턴스 객체의 인스턴스 변수에 들어있는 기존 값을 변경하고 저장
>>> article = Article.objects.get(pk=1)
>>> article.title = 'byebye'
>>> article.save()
```



## DELETE

- delete로 지우고 새로 추가하면, database에서는 기존의 번호가 아닌 저장된 번호 다음 번호로 저장된다.

```python
# article 인스턴스 객체를 생성 후 .delete() 메서드를 호출
>>> article = Article.objects.get(pk=1)
>>> article.delete()
```



- 핵심은 우리는 ORM을 통해 클래스의 인스턴스 객체로 DB를 조작할 수 있다는 것!
- 앞으로 CRUD 로직을 직접 작성하면서 위에서 배운 코드들을 다시 활용하게 될 것이다.



The Django admin site : https://docs.djangoproject.com/en/2.2/ref/contrib/admin/

## ADMIN

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지.
- `models.py`에 작성한 클래스를 `admin.py`에 등록하고 관리.
- record 생성 여부 확인에 매우 유용하고 직접 레코드를 작성할 수도 있다.
- CRUD 로직을 모두 관리자페이지에서 사용할 수 있다.



### 관리자 변경 목록 change list 커스터마이징

1. ##### list_display

   - admin 페이지에서 우리가 `models.py`에 정의한 각각의 속성(컬럼)들의 값(레코드)을 보여준다.

2. list_filter

   - 특정 필드에 의해 변경목록을 필터링할 수 있게 해주는 filter 사이드바를 추가한다.
   - 표시되는 필터의 유형은 필드의 유형에 따라 다르다.

3. list_display_links

   - 목록 내에서 링크로 지정할 필드 적용(설정하지 않으면 기본값을 첫번째 필드에 링크가 적용)

4. list_editable

   - 목록 상에서 직접 수정할 필드 적용

5. list_per_page

   - 한 페이지에 표시되는 항목 수를 제어(기본값 100)

> $ python manage.py createsuperuser



---------------------------

Django Extension : https://django-extensions.readthedocs.io/en/latest/index.html

### Django extensions

- Django-extension은 커스텀 확장 tool이다.

- Django app 구조로 되어 있기 때문에 프로젝트에서 사용하기 위해서는 app 등록과정을 거쳐야 한다.

  

- extention 설치

  > $ pip install django-extensions
  >
  > setting.py에서 INSTALLED_APPS에 'django_extensions', 추가

- shell plus 실행

  > $ python manage.py shell_plus