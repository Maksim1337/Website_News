from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import News
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .forms import NewsForm


class Index(TemplateView):
    template_name = 'main/index.html'


class About(TemplateView):
    template_name = 'main/about.html'


def read(request):
    news_buf = News.objects.order_by('-id')
    return render(request, 'main/news.html', {'title': 'Новости', 'news': news_buf})


def create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
            
    form = NewsForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


class Contacts(TemplateView):
    template_name = 'main/contacts.html'


class Signin(TemplateView):
    template_name = 'main/signin.html'


class LoginView(TemplateView):
    template_name = "main/signin.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)


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


def logout_user(request):
    logout(request)
    return redirect('index')
