Validate : https://docs.djangoproject.com/en/2.2/ref/models/instances/#validating-objects

## CREATE

- views ??

	1. 글을 쓰는 페이지 view(new)
 	2. 작성된 글을 받아서 db에 저장하는 역할을 하는 view(create)



​    TextField()의 경우 대용량의 텍스트를 받기 때문에

기존의 \<input type="text" name="content" id="content"> 대신에

\<textarea name="" id="" cols="30" rows="5">\</textarea> 를 써준다



admin의 list_display를 한번에 등록(거의 쓸 일 없을 것)

> def get_all_fields(self):
>
> ​     return tuple(field.name for field in self._meta.get_fields())
>
>  
>
>  class ArticleAdmin(admin.ModelAdmin):
>
> ​	list_display = get_all_fields(Article)



QuerySet : https://docs.djangoproject.com/ko/2.2/ref/models/querysets/#queryset-api-reference

## READ

- 가능하면 ORM에서 받아서 처리하는 것이 빠른 편(권장)
- Python으로 처리할 수도 있다.
- 글이 보이지 않는 이유는 페이지 자체는 index가 맞지만 url은 아직 create에 머물어 있다. 왜냐하면 페이지는 전환됐지만
- POST방식은 render보다는 redirect방식을 쓴다.
- GET -> POST
  - 글을 작성할 때 GET이 아닌 POST를 쓰는 3가지 이유
    	1. 사용자는 django에게 **HTML 파일을 줘!(GET)** 가 아니라 **~ 한 레코드(글)을 생성해줘!(POST)** 이기 때문에 GET보다는 POST 요청이 더 알맞다.
     	2. 데이터는 URL에 노출되면 안된다. (우리가 URL에 접근하는 방식은 모두 GET). query의 형태를 통해 DB schema를 유추할 수 있게 되고, 이는 보안의 측면에서 매우 취약하게 된다.
     	3. 모델(DB)를 조작하는 친구는 GET이 아닌 POST 요청! 왜냐? DB를 수정하는 건 매우 중요한 일이고, 그에 따른 최소한의 신원 확인이 필요하다!(GET으로 동작하게 된다면, 악성사용자가 URL만으로 글을 작성, 수정, 삭제할 수 있게 된다.)

------------

#### Redirect

- POST 요청은 HTML 문서를 render하는게 아니라. `~~좀 처리해줘(요청)`의 의미이기 때문에 요청을 처리하고 나서의 결과를 보기위한 페이지로 넘겨줘야 한다.



#### POST 요청으로 변경 후 변화하는 것

- form을 통해 전송한 데이터를 받을때도 `request.POST`로 받아야 한다.
- 글이 작성되면 실제로 URL에 데이터가 나타나지 않게 된다.
- html 문서를 요청하는게 아니기 때문에, html 문서를 받아볼 수 있는 다른 페이지로 redirect하게 된다.



## DELETE

- delete의 경우 render로 쓰지 않고, DB를 건들였기 때문에 redirect를 사용.



## UPDATE

1. 수정하는 페이지 view (edit)
2. 직접 모델에 수정 요청을 보내는 view (update)



#### edit page

- input form의 경우 이전 내용을 남겨두고 싶은 경우 받는 article을 value에 추가해 넣어준다.
- textarea의 경우 value가 아닌 태그 안의 내용으로 넣어줘야한다.

