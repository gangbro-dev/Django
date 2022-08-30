from xmlrpc.client import APPLICATION_ERROR
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def greeting(request):
    a = request.GET.get('NAME')
    if a == None:
        a = ''
    print(a)
    content = {
        'name': 'Alice',
        'NAME': a,
    }
    return render(request, 'greeting.html', content)


def peek(request):
    a = request.GET.get('NAME')
    
    print('message=', a)
    content = {
        'name': 'Alice',
        'NAME': a,
    }
    return render(request, 'peek.html', content)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)