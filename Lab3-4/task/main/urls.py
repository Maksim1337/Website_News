from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('news', views.news),
    path('contacts', views.contacts),
    path('signin', views.signin)
]
