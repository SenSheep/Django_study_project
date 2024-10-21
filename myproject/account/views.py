from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Transaction

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Перенаправление на домашнюю страницу после регистрации
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('transaction')  # Перенаправление на домашнюю страницу после входа
        else:
            messages.error(request, "Неверное имя пользователя или пароль.")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')  # Перенаправление на домашнюю страницу после выхода

@login_required
def transaction(request):
    user = request.user  # Получаем текущего пользователя
    user_id = user.id + 1000  # Получаем его уникальный ID
    transactions = Transaction.objects.filter(user=user).order_by('-date')  # Получаем транзакции текущего пользователя
    return render(request, 'transaction.html', {'transactions': transactions, 'user_id': user_id})