from io import open_code
from django.http import HttpResponse
from django.shortcuts import render
import string
import random
import os
from django.contrib.auth.models import User,auth 

def quiz(request):
    return render(request, 'quiz.html')

def javaQuiz(request):
    return render(request, 'javaquizpage.html')

def pythonQuiz(request):
    return render(request, 'pythonquizpage.html')

def cppQuiz(request):
    return render(request, 'cppquizpage.html')