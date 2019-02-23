from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.appEgresados, name='post_list'),
]