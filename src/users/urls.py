from django.urls import path
from .views import  logout, Login, CreateUser, Decode_Token, DetailUser
from . import  views

urlpatterns = [
    path('logout',logout, name='logout'),
    path('login', Login.as_view()),
    path('create', CreateUser.as_view()),
    path('decode-token', Decode_Token.as_view()),
    path('<uuid:pk>', DetailUser.as_view()),
]

