from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.posts, name="posts"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('create-post/', views.create_post, name='create-post'),
    path('<slug:slug>/', views.post, name='single-post'),
    path('<slug:slug>/update/', views.update_post, name='update-post'),
    path('<slug:slug>/delete/', views.delete_post, name='delete-post'),
]
