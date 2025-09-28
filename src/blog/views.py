from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Post


def home(request: HttpRequest) -> HttpResponse:
    return render(
        request, 'blog/home.html', {'posts': Post.objects.order_by('-date_posted')}
    )


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/about.html', {'title': 'About'})
