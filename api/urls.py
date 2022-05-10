from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUser),
    path('getIP/', views.getIP),
    path('updateIP/', views.updateIP)
]