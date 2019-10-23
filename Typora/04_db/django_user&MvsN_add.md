### profile

- user관련 사항은 urls.py에서 가장 아래로 내려야한다! => 그렇지 않으면 위에서 아래로 읽어가는 특성 상 그 밑의 함수들이 동작하지 않음.



## `with` template tag

- 복잡한 변수를 더 간단한 이름으로 저장(캐시)하며, 여러번 DB를 조회할 때(특히 비용이 많이 드는) 유용하게 사용가능하다.

> {% with articles=person.article_set.all %} => 이것을 우선
>
> {% with person.article_set.all as articles %}



### 조기 최적화는 프로그래밍에서 악의 근원

### 코드는 코드 자체적으로도 빨라야 하지만,  더 중요한 것은 다른 개발자들이 읽기 쉬워야한다.



# M:N FOLLOW

## User : User

- settings.py에서 기존에는 `AUTH_USER_MODEL = 'auth.User'`가 기본 default였는데,  `AUTH_USER_MODEL = 'accounts.User'`로 변경해준다.
- 그 전까지는 accounts의 forms에서 model을 상속받았기 때문에, Meta에서의 model은 생략했었지만, 활성화된 user를 받는 `get_user_model()`로 바꿔준다.