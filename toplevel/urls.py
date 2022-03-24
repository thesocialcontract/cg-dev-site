from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404/', views.http404, name='http404'),
    path('500/', views.http500, name='http500'),
]