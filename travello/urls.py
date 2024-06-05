from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('user_login', views.user_login, name='user_login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
    path('register', views.register, name='register'),
]