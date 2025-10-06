from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm


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
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=profile_user)
        profile_update_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=profile_user.profile
        )
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(
                request, 'Your account has been updated!'
            )
            return redirect('users-profile', username=profile_user.username)

    else:
        user_update_form = UserUpdateForm(instance=profile_user)
        profile_update_form = ProfileUpdateForm(instance=profile_user.profile)

    context = {
        'profile_user': profile_user,
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form,
    }

    return render(request, 'users/profile.html', context)
