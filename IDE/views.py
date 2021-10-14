from io import open_code
from django.http import HttpResponse
from django.shortcuts import render
import string
import random
import os
from .models import Questions
from django.contrib.auth.models import User,auth 

# Create your views here.
def home(request):
    return render(request, 'homepage.html')


def enterIDE(request):
    question = ""
    firstName=""
    if request.method == 'POST':
        firstName = request.POST['firstName']
    else:
        pass
    if firstName == 'Manish':
        question = Questions.objects.filter(
            difficulty_level='DIFFICULT').first()
    else:
        question = Questions.objects.filter(
            difficulty_level='EASY').first()
        
    return render(request, 'ide.html', {'firstName': firstName, 'question': question})


def executeCode(request):
    output = ""
    language = request.GET['language'].lower()
    code = request.GET['code']
    print("language:            "+language)
    print("Code:            "+code)
    randomName = ''.join(random.choices(string.ascii_lowercase, k=7))
    print("randomName:            "+randomName)
    filePath = "IDE/tempCodes/"+randomName+"."+language
    print("filePath:            "+filePath)

    f = open(filePath, "w+")
    f.write(code)
    f.close()
    
    return render(request,'ide.html')
    
   