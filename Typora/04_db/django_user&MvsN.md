## User - Article

- 1 : N 관계
- settings.py에서 `AUTH_USER_MODEL = 'auth.User'`가 default라서 기본적으로 생략되어 있음.



## django가 서버가 켜질 때 초기화 순서

1. ##### `INSTALLED_APPS`의 각 항목을 import 합니다. (위에서 아래로!)

   - 이 과정에서 직간접적으로 모델을 import해선 안된다.
   - 1번 단계에서 app을 import하는 동안에 불필요한 제약들을 피하기 위해 이 단계에서는 모델을 가져오지 않는다.

2. ##### 각 어플리케이션의 models를 import 한다.

   - 2단계가 완료가 되면, `get_model()`과 같은 모델에서 작동하는 APIs를 사용할 수 있게 된다.

3. ##### `AppConfig`의 ready() 메서드를 실행한다.



#### models.py에서 `get_user_model()`을 쓸 경우 발생하는 일

1. 1단계에 articles부터 import 시작

2. 2단계에서 articles부터 model을 import 시작
3. 2단계에서 accounts에서 model을 import 시작 ??? 에러!



- 2단계가 완료된 후에야 get_user_model()을 사용할 수 있는데 아직 accounts app이 INSTALLED_APP의 작성 순서때문에 아직 IMPORT가 완료되지 않은 상황이라 get_user_model()이 어떤 User model을 return해야 하는지 django가 알 수 없는 상태이다.



`get_user_model()`

- return 값이 `class`

`settings.AUTH_USER_MODEL`

- return 값이 `str`



##### 결론

- 모든 곳에서 User model을 호출할 때는 `get_user_model()`
- 단, `models.py`에서만 `settings.AUTH_USER_MODEL`



## gravatar 프로필 이미지

1. ModelForm Custom
2. Custom template tags and filters

{{ email | ssafy }} => 해시값

---------------------------

# Model Relation

### Model relationships

1. Many-to-one
2. Many-to-many

#### User : Article = M : N

- User는 여러 개의 Article에 LIKE 할 수 있고
- Article은 여러 User로부터 LIKE 받을 수 있다.



#### 모델링은 현실 세계를 최대한 유사하게 반영하기 위해서 해야한다.

-------------------------------------------

환자와 의사의 예약 시스템을 구축하려는 프로젝트

의사 1 : 환자 N

1. 1:N의 한계
2. 중개모델 생성
3. 중개 모델을 직접 거치지 않고 바로 가져올 수는 없을까?
   - `Through` option
   - MTOM 필드는 실제 물리적인 필드가 db에 생기는 것이 아니다.
4. Doctor도 patients로 참조할 수 없을까?
   - `related_name`
     - 참조되는 대상이 참조하는 대상을 찾을 때(역참조), 어떻게 불러 올지에 대해 정의한다.
     - 필수적으로 사용하는 건 아니지만, 필수적인 상황이 발생할 수 있다.

--------------------------

### 중개모델은 필요없는가?? 아니다.

- 예약한 시간 정보를 담는다거나 하는 경우(추가적인 필드가 필요한 경우)에는 반드시 중개모델을 만들어서 진행을 해야되는 상황도 있다. 다만 그럴 필요가 없는 경우 위와 같이 해결할 수 있다.

------------------------------------



## LIKE

- user는 여러 article에 좋아요를 누를 수 있고
- article은 여러 user로부터 좋아요를 받을 수 있다.

`article.user` => 게시글을 작성한 유저 - 1: N

`article.like_users` => 게시글을 좋아요한 유저 - M : N

`user.like_articles` => 유저가 좋아요를 누른 게시글(역참조, related_name) - M : N

`user.article_set` => 유저가 작성한 게시글(역참조) - 1 : N