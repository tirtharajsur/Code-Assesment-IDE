from io import open_code
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
import string
import random
import os

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def enterIDE(request):
    if request.method =='POST':
        firstName = request.POST['firstName']
    else:
        pass
    
    return render(request, 'ide.html',{'firstName':firstName})

def executeCode(request):
    if request.method =='POST':
        
        print(request.POST)
        language = request.POST['language'].lower()
        code = request.POST['code']
        randomName = ''.join(random.choices(string.ascii_lowercase,k = 7))
        filePath = "IDE/tempCodes/"+randomName+"."+language

        f= open(filePath,"x")
        f.write(code)
        f.close() 
         
        with open(filePath, 'w+') as fp:
             fp.write(code)
        # FileToBeExecuted = open(filePath,"w")
        # FileToBeExecuted.write(code)
        # FileToBeExecuted.close()
        
        # C:\Users\Tirtha\AppData\Local\Programs\Python\Python39\python.exe
        
    else:
        pass
    
    return render(request,'ide.html')
     
    
   