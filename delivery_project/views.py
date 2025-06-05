from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна!')
            return redirect('index')  # Перенаправление на главную страницу
        else:
            messages.error(request, 'Ошибка при регистрации')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})