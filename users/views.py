from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def profile_update(request):
    if request.method == 'POST':
        u_user = UserUpdateForm(request.POST, instance=request.user)
        p_user = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_user.is_valid() and p_user.is_valid():
            u_user.save()
            p_user.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        u_user = UserUpdateForm(instance=request.user)
        p_user = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_user': u_user,
        'p_user': p_user,
    }
    return render(request, 'users/profile_update.html', context)
