from django.shortcuts import render
from .models import News
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm


class Index(TemplateView):
    template_name = 'main/index.html'


class About(TemplateView):
    template_name = 'main/about.html'


def news(request):
    news_buf = News.objects.order_by('-id')
    return render(request, 'main/news.html', {'title': 'Новости', 'news': news_buf})


class Contacts(TemplateView):
    template_name = 'main/contacts.html'


class Signin(TemplateView):
    template_name = 'main/signin.html'


class Signup(TemplateView):
    template_name = 'main/signup.html'


class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'main/signup'


