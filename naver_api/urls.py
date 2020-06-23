
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('naver_api/', views.naver_api, name='naver_api'),
]
