from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    # artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musics')   # 다른 이름으로 바꿀때 첫번째 방법
    title = models.TextField()

    def __str__(self):
        return self.title

    
class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
    