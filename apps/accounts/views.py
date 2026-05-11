from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser

# Home page
def home(request):
    return render(request, 'home.html')

# Registration
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm = request.POST['password2']
        user_type = request.POST.get('user_type', 'freelancer')  # default freelancer

        if password != confirm:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            user_type=user_type
        )
        login(request, user)
        messages.success(request, 'Registration successful')
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
            messages.success(request, f'Welcome {username}')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')

# Logout
def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out')
    return redirect('login')

# Static pages
def learn_more(request):
    return render(request, 'learn_more.html')

def support(request):
    return render(request, 'support.html')