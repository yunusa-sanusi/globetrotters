from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='blog-home'),
    path('destinations/', include('destination.urls')),
    path('posts/', views.posts, name="posts"),
    path('post/<slug:slug>', views.post, name='single-post'),
]
