from django.urls import path
from . import views


urlpatterns = [
    path('', views.destinations, name='destinations'),
    path('add-destination', views.add_destination, name='add-dst'),
    path('<slug:slug>/', views.single_destination, name='single-dst'),
    path('<slug:slug>/update', views.update_destination, name='update-dst'),
    path('<slug:slug>/remove', views.remove_destination, name='remove-dst'),
]
