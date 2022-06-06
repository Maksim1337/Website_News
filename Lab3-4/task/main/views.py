from django.shortcuts import render
from .models import News


def index(request):
    newsbuf = News.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная', 'news': newsbuf})


def about(request):
    return render(request, 'main/about.html')


def news(request):
    newsbuf = News.objects.order_by('-id')
    return render(request, 'main/news.html', {'title': 'Новости', 'news': newsbuf})
