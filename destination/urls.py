from django.urls import path
from . import views


urlpatterns = [
    path('', views.destinations, name='destinations'),
    path('<slug:slug>/', views.single_destination, name='single-dst'),
]
