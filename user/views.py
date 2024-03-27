from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib.auth import login, authenticate, logout

from .models import CustomUser


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = CustomUser.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect('home_book')
    else:
        form = SignUpForm()
    return render(request, 'login/register.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_book')
    else:
        form = SignInForm()
    return render(request, 'login/login.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('login')
