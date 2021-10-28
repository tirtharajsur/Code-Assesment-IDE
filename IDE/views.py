from django.views.decorators.csrf import csrf_exempt
from io import open_code
from django.http import HttpResponse
from django.shortcuts import render
import string
import random
import os
from .models import Questions
from django.contrib.auth.models import User, auth
from .JudgeAPI import submitRequest
from django.http.response import JsonResponse


# Create your views here.


def home(request):
    return render(request, 'homepage.html')


def enterIDE(request):
    question = ""
    firstName = ""
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


@csrf_exempt
def executeCode(request):
    print(request)
    language = request.POST.get('language')
    code = str(request.POST.get('code')).replace("\\r\\n", "")
    print("language:            "+language)
    print("Code:            "+code)

    response = submitRequest(71, code)
    print(response)
    print(response.keys())
    # randomName = ''.join(random.choices(string.ascii_lowercase, k=7))
    # print("randomName:            "+randomName)
    # filePath = "IDE/tempCodes/"+randomName+"."+language
    # print("filePath:            "+filePath)

    # f = open(filePath, "w+")
    # f.write(code)
    # f.close()
# render(request, 'ide.html', response)
    return JsonResponse({'success': response.get("stdout"), 'errorMsg': response.get("stderr")})
