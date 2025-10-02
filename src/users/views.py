from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import UserRegisterForm


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your account has been created! You are now able to log in'
            )
            return redirect('users-login')
    elif request.method == 'GET':
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def profile(request: HttpRequest, username=str) -> HttpResponse:
    profile_user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {'profile_user': profile_user})
