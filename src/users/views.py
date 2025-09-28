from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user.username}')
            return redirect('blog-home')
    elif request.method == 'GET':
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
