
from django.urls import path
from . import views
from .views import QuestionListView

app_name = 'polls'
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path("", views.question_list, name= "question_list"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/questions/', QuestionListView.as_view(), name='questions-api'),
]
