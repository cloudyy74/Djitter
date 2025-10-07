from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
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
    path(
        'password-reset/',
        PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset',
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'
        ),
        name='password_reset_confirm',
    ),
    path(
        'password-reset-complete/',
        PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'
        ),
        name='password_reset_complete',
    ),
    path(
        'password-reset/done',
        PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done',
    ),
    path('<str:username>/', views.profile, name='users-profile'),
]
