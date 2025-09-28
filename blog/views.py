from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/home.html')


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>About Djitter<h1>')
