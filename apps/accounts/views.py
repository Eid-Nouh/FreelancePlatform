from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser

def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user_type = request.POST.get('user_type')

        if password1 != password2:
            messages.error(request, 'كلمة المرور غير متطابقة')
            return redirect('register')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'اسم المستخدم موجود مسبقاً')
            return redirect('register')

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password1,
            user_type=user_type
        )
        login(request, user)
        messages.success(request, 'تم التسجيل بنجاح')
        return redirect('home')

    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'مرحباً {username}')
            return redirect('home')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'تم تسجيل الخروج')
    return redirect('login')


def learn_more(request):

    return render(request, 'learn_more.html')

def support(request):

    return render(request, 'support.html')