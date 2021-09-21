
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('enterIDE',views.enterIDE,name='enterIDE'),
    path('quiz',views.quiz,name='quiz'),
    path('javaQuizPage',views.javaQuiz,name='javaQuizPage'),
    path('pythonQuizPage',views.pythonQuiz,name='pythonQuizPage'),
    path('cppQuizPage',views.cppQuiz,name='cppQuizPage'),
    
]
