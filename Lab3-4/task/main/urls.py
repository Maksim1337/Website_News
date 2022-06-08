from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', Index.as_view()),
    path('about', About.as_view()),
    path('news', NewsCl.as_view()),
    path('contacts', Contacts.as_view()),
    path('signin', Signin.as_view()),
    path('signup', Signup.as_view())
]
