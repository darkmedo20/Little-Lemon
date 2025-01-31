from django.urls import path
from django.contrib import admin
from .views import sayHello
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('',sayHello, name="sayHello"),
]