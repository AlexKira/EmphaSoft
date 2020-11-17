from django.urls import path, include
from myapp import views
from django.contrib.auth import views as auth_views
from django.urls import re_path

app_name = 'myapp'


urlpatterns = [

    re_path("home/", views.home, name="home"),
    re_path("account/", views.account, name="account"),
    re_path("index/", views.index, name="index"),
]
