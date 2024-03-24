from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import custom_logout

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('posts/<str:pk_test>/', views.posts, name='posts'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
]