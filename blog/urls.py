from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='blog-home'),
    path('posts/', views.posts, name="posts"),
    path('post/<slug:slug>', views.post, name='single-post'),
]
