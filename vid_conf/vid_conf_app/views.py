from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'success': "Registration successful. Please login."})

        else:
            error_msg = form.errors.as_text()
            return render(request, 'register.html', { 'error': error_msg })

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        email =request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            return render(request, 'login.html', {'error': "Invalid Credentials. Please try again."})

    return render(request, 'login.html')



@login_required
def dashboard(request):
    return render(request, 'dashboard.html', { "name" : request.user.first_name })


@login_required
def videocall(request):
    return render(request, 'videocall.html', {'name' : request.user.first_name + '' + request.user.last_name})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect(f'/meeting?roomID={roomID}')

    return render(request, 'join_room.html', {'name': request.user.first_name + '' + request.user.last_name})