from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import path

from . import views


def root_redirect(request: HttpRequest) -> HttpResponse:
    return redirect('blog-home')


urlpatterns = [
    path('home/', views.PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('', root_redirect, name='blog-root'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='blog-post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='blog-post-create'),
    path(
        'post/<int:pk>/update/', views.PostUpdateView.as_view(), name='blog-post-update'
    ),
    path(
        'post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='blog-post-delete'
    ),
    path(
        'users/<str:username>/posts/',
        views.UserPostListView.as_view(),
        name='blog-user-posts',
    ),
]
