from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import CustomUser


# Home page
def home(request):
    return render(request, 'Home.html')


# Registration
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm = request.POST['password2']

        if password != confirm:
            error = 'Passwords do not match'
            return render(request, 'accounts/register.html', {'error': error})

        if CustomUser.objects.filter(username=username).exists():
            error = 'Username already taken'
            return render(request, 'accounts/register.html', {'error': error})

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            user_type='freelancer'
        )
        login(request, user)
        return redirect('home')

    return render(request, 'accounts/register.html')


# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error = 'Invalid username or password'
            return render(request, 'accounts/login.html', {'error': error})

    return render(request, 'accounts/login.html')


# Logout
def logout_view(request):
    logout(request)
    return redirect('login')


# Static pages
def learn_more(request):
    return render(request, 'learn_more.html')

def support(request):
    return render(request, 'support.html')