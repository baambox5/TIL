# REST API

- 정해진 형식으로 요청을 보내면 요청한 정보를 받을 수 있는 소통 방법.
- 각 요청이 어떠한 동작&정보를 위한 것인지 요청 형식 자체로 파악이 가능한 것.



- 협업할 시 데이터베이스 덮어씌우기

> $ python manage.py dumpdata musics > dummy.json

- 들여쓰기 시켜서 덮어씌우기

> $ python manage.py dumpdata --indent 2 musics > dummy.json



## 덮어쓴 것을 사용하기

### fixture

- 데이터베이스의 직렬화(serialized) 된 내용을 포함하는 파일 모음이다.
- 각 fixture는 고유한 이름을 가지며, 이를 구성하는 파일은 여러 응용 프로그램에서 여러 디렉토리에 배포될 수 있다.
- django는 `loaddata`시 설치된 모든 app에서 `fixtures`라는 이름의 폴더를 찾는다.

```
musics/ (앱)
	fixtures/
		musics/ (앱 이름)
			dummy.json
```

- dummy.json을 위의 해당 위치로 이동시켜서 아래 명령어를 입력해 load한다.

> $ python manage.py loaddata musics/dummy.json



- 창에 뜨는 이름 바꾸기

> 첫번째 방법
>
> \# models.py
>
> artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musics') 
>
> \# 이 방법은 db migration해야함.

> 두번째 방법
>
> \# serializers.py
>
> class ArtistDetailSerializer(ArtistSerializer):
>
>   musics = MusicSerializer(source='music_set', many=True)
>
> \# 기존에 music_set을 music으로 바꾸고 싶을때 source로 바꿔줌. 최근에는 source를 안 써도 제대로 동작함.