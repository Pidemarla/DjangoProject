from django.urls import path

from . import views

urlpatterns = [
    path('calc', views.home, name='home'),
    path('add', views.add, name='add'),
]