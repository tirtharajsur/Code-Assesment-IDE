from io import open_code
from django.http import HttpResponse
from django.shortcuts import render
import string
import random
import os

# Create your views here.
def home(request):
    #return HttpResponse("Hello World")
    return render(request, 'homepage.html')

def enterIDE(request):
    if request.method =='POST':
        firstName = request.POST['firstName']
    else:
        pass
    
    return render(request, 'ide.html',{'firstName':firstName})

def executeCode(request):
    if request.method =='POST':
        language = request.POST['language'].lower()
        code = request.POST['code']
        code = request.POST['']
        randomName = string.ascii_lowercase
        filePath = "tempCodes/"+randomName+"."+language
        with open(filePath, 'w') as fp:
            pass
        # FileToBeExecuted = open(filePath,"w")
        # FileToBeExecuted.write(code)
        # FileToBeExecuted.close()
        
        
    else:
        pass
    
    return render(request,'ide.html')
    
   