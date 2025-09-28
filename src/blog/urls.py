from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import path

from . import views


def root_redirect(request: HttpRequest) -> HttpResponse:
    return redirect('/home/')


urlpatterns = [
    path('home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('', root_redirect, name='blog-root'),
]
