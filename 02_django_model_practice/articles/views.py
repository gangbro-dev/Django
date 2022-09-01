from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # 사용자의 데이터를 받아서 DB에 저장
    title = request.POST.get('title')
    content = request.POST.get('content')
    # DB에 저장
    # 1번 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2번 방법 **추천**
    article = Article(title=title, content=content)
    article.save()

    # 3번 방법
    # Article.objects.create(title=title, content=content)
    return redirect('articles:detail', article.pk)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()
    return redirect('articles:detail', article.pk)


def delete(request, aa):

    # pk 이용해서 아티클 찾기
    article = Article.objects.get(pk=pk)

    article.delete()

    return redirect('articles:index')
