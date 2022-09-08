from django.shortcuts import render, redirect
<<<<<<< HEAD
=======
from django.views.decorators.http import require_safe, require_http_methods, require_POST
>>>>>>> 4e59eac205cc821d21b2a8a957f741db3d61c8e8
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
<<<<<<< HEAD
    # 사용자의 데이터를 받아서 DB에 저장
    title = request.POST.get('title')
    content = request.POST.get('content')
    # DB에 저장
    # 1번 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
=======
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article)
    else:
        # new
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
>>>>>>> 4e59eac205cc821d21b2a8a957f741db3d61c8e8


<<<<<<< HEAD
    # 3번 방법
    # Article.objects.create(title=title, content=content)
    return redirect('articles:detail', article.pk)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
=======
@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
>>>>>>> 4e59eac205cc821d21b2a8a957f741db3d61c8e8
    }
    return render(request, 'articles/detail.html', context)


<<<<<<< HEAD
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
=======
@require_POST
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # update
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        #edit
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
>>>>>>> 4e59eac205cc821d21b2a8a957f741db3d61c8e8
