from io import open_code
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
import string
import random
import os
from pathlib import Path

# from IDE.tempCodes import *

# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent


def home(request):
    return render(request, 'homepage.html')


def enterIDE(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
    else:
        pass
    if firstName == 'Manish':
        question = Questions.objects.filter(
            difficulty_level='EASY').findfirst()
    else:
        question = Questions.objects.filter(
            difficulty_level='DIFFICULT').findfirst()
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

    # C:\Users\Tirtha\AppData\Local\Programs\Python\Python39\python.exe
    # if(language == "py"):
    # output = os.system(filePath)

    # if request.method =='POST':

    #     print(request.POST)
    #     language = request.POST['language'].lower()
    #     code = request.POST['code']
    #     print("language:            "+language)
    #     print("Code:            "+code)
    #     randomName = ''.join(random.choices(string.ascii_lowercase,k = 7))
    #     filePath = "IDE/tempCodes/"+randomName+"."+language
    #     fileName = os.path.join(BASE_DIR,'template')+randomName+"."+language
    #     print("File name: "+fileName)

    #     f= open(fileName,"w")
    #     f.write(code)
    #     f.close()

    #     # with open(filePath, 'w+') as fp:
    #     #      fp.write(code)
    #     # FileToBeExecuted = open(filePath,"w")
    #     # FileToBeExecuted.write(code)
    #     # FileToBeExecuted.close()

    #     # C:\Users\Tirtha\AppData\Local\Programs\Python\Python39\python.exe
    #     if(language == "py"):
    #         output = os.system("python filePath.py")

    # else:
    #     pass

    return render(request, 'ide.html', {'output': output})
