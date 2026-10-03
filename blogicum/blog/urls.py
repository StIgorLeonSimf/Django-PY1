
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_post/', views.post, name='create_post'),
    path('edit_post/<int:pk>/', views.post, name='edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('post_seek/', views.post_seek, name='post_seek'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('category/<int:pk>/', views.category, name='category'),
]
