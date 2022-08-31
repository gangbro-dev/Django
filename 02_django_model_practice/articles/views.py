from django.shortcuts import render
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
    title = request.GET.get('title')
    content = request.GET.get('content')
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
    return render(request, 'articles/create.html')