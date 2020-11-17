from myapp import views
from django.urls import re_path
from . import views

from django.urls import path

app_name = 'forms'

urlpatterns = [

    path('forms/',views.image, name='forms'),
    

]
