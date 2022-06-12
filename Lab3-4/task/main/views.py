from django.shortcuts import redirect, render
from django.urls import reverse
from .models import News
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class RegisterView(TemplateView):
    template_name = "main/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse('index'))

        return render(request, self.template_name)
