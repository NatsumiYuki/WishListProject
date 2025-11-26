from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .loginform import LoginForm


def home(request):
    return render(request, "home.html")


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'usuario/login.html', {'form': form})

