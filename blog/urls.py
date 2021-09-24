from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='blog-home'),
    path('destinations/', include('destination.urls')),
    path('posts/', views.posts, name="posts"),
    path('create-post/', views.create_post, name='create-post'),
    path('post/<slug:slug>/', views.post, name='single-post'),
    path('post/<slug:slug>/update/', views.update_post, name='update-post'),
    path('post/<slug:slug>/delete/', views.delete_post, name='delete-post'),
]
