from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('julia', views.julia, name='julia'),
]