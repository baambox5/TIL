from django.db import models

# Create your models here.
class Article(models.Model):    # models.Model의 상속을 받는다.
    # id(프라이머리 키)는 기본적으로 처음 테이블 생성시 자동으로 만들어진다.
    # id = models.AutoField(primary_key=True)     # id란 명목의 열 만들기
    title = models.CharField(max_length=10)     # 클래스 변수(DB의 필드). title이란 명목의 열에서 제목은 최대 10글자까지만 쓰겠다는 것
    content = models.TextField()                # 클래스 변수(DB의 필드). 무한정 들어갈 수 있음
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}번글 - {self.title} : {self.content}'