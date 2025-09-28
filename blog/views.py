from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

posts = [
    {
        'author': 'cat_cucumber',
        'title': 'post 1',
        'content': 'first post',
        'date_posted': 'September 28, 2025',
    },
    {
        'author': 'cat_tomato',
        'title': 'post 2',
        'content': 'second post',
        'date_posted': 'September 29, 2025',
    },
]


def home(request: HttpRequest) -> HttpResponse:
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/about.html')
