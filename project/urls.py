"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #home
    path('',base),
    path('home',home,name='home'),

    #book
    path('book_list',book_list,name='book_list'),
    path('book_detail',book_detail,name='book_details'),
    path('add_book',add_book,name='book_form'),

    #author
    path('author_list',author_list,name='author_list'),

    #member
    path('member_list',member_list,name='member_list'),
    path('add_member',add_member,name='member_form'),
]
