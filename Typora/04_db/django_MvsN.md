# Hashtag

- 수정될 때는 게시글의 hasgtag 전체를 삭제한 후 다시 등록하는 과정이 필요하다.



## get_or_create(defaults=None, **kwargs)

- 주어진 kwargs로 객체를 찾으며 필요한 경우 하나를 만든다.
- `(object, created)` 형태의 튜플을 리턴한다.
- object는 검색 또는 생성된 객체이고, created는 새 객체 생성여부를 지정하는 boolean값이다. (새로 만들어진 object라면 True, 기존에 존재하던 object라면 False)
- 단, 이 메서드는 DB가 키워드 인자의 `unique` 옵션을 강제하고 있다고 가정하고 실행한다. (혹시 모를 중복 오브젝트를 방지하기 위함)
- 이는 요청이 병렬로 작성될 때 및 중복 코드에 대한 문제 방지로 중복 오브젝트가 작성되는 것을 예방한다.



### unique

- True인 경우, 이 필드는 테이블 전체에서 고유한 값이어야 한다.
- 유효성 검사 단계에서 실행되며, 중복 값이 있는 모델을 저장하려고 하면, .save() 메서드로 인해 `IntegrityError`가 발생한다.
- ManyToManyField 및 OneToOneField를 제외한 모든 필드 유형에서 유효하다.



### tag escape / html escape

- html창에서는 link가 걸리지 않고 html구문 그대로 보이는 경우가 있다.
- 그것을 의도한 대로 link가 걸리도록 함.

> \<p>{% autoescape off %} {{ article|hashtag_link }} {% endautoescape %}</p>
>
> \<p>{{ article|hashtag_link|safe }}</p>



### OAuth

- 비밀번호를 입력해서 직접 가입하지 않고 외부의 사이트 로그인과 연동해 로그인 