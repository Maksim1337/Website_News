from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about', About.as_view()),
    path('news', views.news),
    path('contacts', Contacts.as_view()),
    path('signup', RegisterView.as_view()),
    path('signin', LoginView.as_view()),
    path('create', views.create),
    path('logout', views.logout_user),
]
