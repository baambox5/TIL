from IPython import embed
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Article, Comment

# Create your views here.
def index(request):
    # articles = Article.objects.all()    
    articles = Article.objects.order_by('-pk') # DB가 변경(가능한 권장)
    # articles = Article.objects.all()[::-1] # python이 변경
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)


def create(request):
    # CREATE
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        # 1
        # article = Article()
        # article.title = title
        # article.content = content
        # article.save()

        # 2
        article = Article(title=title, content=content, image=image)
    
        article.save()
        # 3
        # Article.objects.create(title=title, content=content)

        return redirect(article) # 메인 페이지
        # return redirect('/articles/', article.pk)
    # NEW
    else:
        return render(request, 'articles/create.html')


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    context = {'article': article, 'comments': comments,}
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':        
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.image = request.FILES.get('image')
        article.save()
        return redirect(article)
    else:
        context = {'article': article,}
        return render(request, 'articles/update.html', context)


def comments_create(request, article_pk):
    # 댓글을 달 게시글
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        # form에서 넘어온 댓글 정보
        content = request.POST.get('content')
        # 댓글 생성 및 저장
        comment = Comment(article=article, content=content)
        comment.save()
        return redirect(article)
        # return redirect('articles:detail', article.pk)
        # return redirect('articles:detail' article_pk)
    else:
        return redirect(article)


def comments_delete(request, article_pk, comment_pk):
    # article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    # return redirect(article)
    return redirect('articles:detail', article_pk)