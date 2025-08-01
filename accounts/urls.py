from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
