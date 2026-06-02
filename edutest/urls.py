"""
URL configuration for edutest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from exams import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('login/', views.login),
    path('register/', views.register),
    path('dashboard/', views.dashboard),
    path('history/', views.history),
    path('leaderboard/', views.leaderboard),
    path('exam/<int:exam_id>/', views.exam, name='exam'),
    path('logout/', views.logout_user,name='logout'),
]