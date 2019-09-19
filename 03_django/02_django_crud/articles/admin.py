from django.contrib import admin
from .models import Article, Comment

# Register your models here.
# def get_all_fields(self):
#     return tuple(field.name for field in self._meta.get_fields())


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    # list_display = get_all_fields(Article)
admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at', 'article_id',)
admin.site.register(Comment, CommentAdmin)