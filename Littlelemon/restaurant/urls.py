
from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.MenuItemsView.as_view()),
    path('<int:pk>', views.SingleMenuItemView.as_view()),
]