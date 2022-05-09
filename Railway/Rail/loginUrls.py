from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('', views.index,name="login"),
   path('home/',views.Home),
   path('loginError/',views.login_errors,name="loginError"),
   path('register/',views.registerUser,name = "registerUser")
]