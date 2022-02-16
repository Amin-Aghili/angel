from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in!', 'success')
                return redirect('shop:home')
            else:
                messages.error(request, 'Your email or password is incorrect!', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!', 'success')
    return redirect('shop:home')


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = CustomUser.objects.create_user(cd['email'], cd['first_name'], cd['last_name'], cd['password'])
            user.save()
            messages.success(request, 'You have successfully registered!', 'success')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})