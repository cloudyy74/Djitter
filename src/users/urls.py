from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='users-register'),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='users-login',
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='users-logout',
    ),
    path('<str:username>/', views.profile, name='users-profile'),
]
