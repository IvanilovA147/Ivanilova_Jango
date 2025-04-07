# Create your views here.

from .models import Question
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm, UserLoginForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserLoginForm


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


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('http://127.0.0.1:8000/polls/')  # або будь-яка інша сторінка
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
                return redirect('http://127.0.0.1:8000/polls/')  # або будь-яка інша сторінка
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # або 'home'


class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()  # Отримуємо всі питання з бази даних
        serializer = QuestionSerializer(questions, many=True)  # Серіалізуємо питання
        return Response(serializer.data, status=status.HTTP_200_OK)  # Повертаємо дані у форматі JSON
