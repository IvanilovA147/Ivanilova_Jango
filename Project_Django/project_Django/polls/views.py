# Create your views here.

from .models import Question
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm


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
