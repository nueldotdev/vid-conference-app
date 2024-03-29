from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('meeting/', views.videocall, name="meeting"),
    path('join/', views.join_room, name="join"),
]