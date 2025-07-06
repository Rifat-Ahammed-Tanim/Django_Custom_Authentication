from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import *

@login_required
def home(request):
    return render(request, 'home_page.html')

# Registration Functionality
def register_page(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            CustomUser.objects.create_user(
                username=request.POST.get('username'),
                password=password,
                full_name=request.POST.get('full_name'),
                email=request.POST.get('email'),
                mobile_number=request.POST.get('mobile_number'),
                gender=request.POST.get('gender'),
                age=request.POST.get('age'),
                date_of_birth=request.POST.get('date_of_birth'),
                present_address=request.POST.get('present_address'),
                profile_image=request.FILES.get('profile_image'),
            )
            return redirect('login')
    return render(request, 'register_page.html')

# Login Functionality
def login_page(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login_page.html')

# Logout Functionality
def logout_page(request):
    logout(request)
    return redirect('login')

    

