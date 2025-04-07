# Create your views here.

from .models import Question
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm, UserLoginForm




def question_list(request):
    # Отримуємо всі питання з моделі Question
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'question_list.html', context)

def register_view(request):
    if request.method == "POST":
        # Створення форми з переданими даними POST
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Збереження нового користувача та входження в систему
            user = form.save()
            login(request, user)
            # Перенаправлення на домашню сторінку після успішної реєстрації
            return redirect('http://127.0.0.1:8000/polls/')
    else:
        # Якщо метод не POST, то створюємо порожню форму
        form = RegistrationForm()

    # Повертаємо форму в шаблон
    return render(request, 'register.html', {"form": form})


# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserLoginForm


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # або будь-яка інша сторінка
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # або 'home'


# views.py
def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # або будь-яка інша сторінка
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # або 'home'
