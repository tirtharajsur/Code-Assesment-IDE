from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth 
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        
        if password == confirm_password:
            
            if User.objects.filter(username=username).exists():
                messages.info(request,'Warning!Username already taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Warning! Email already registered with other username!')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
                user.save()
                messages.info(request,'Success! You are Registered.')
            return redirect('register')
        else:
            messages.info(request,'Warning! Password not matching!')
        return redirect('register')
                
    else:
        return render(request, 'login.html')
    
    
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('usernameLogin')
        password = request.POST.get('passwordLogin')
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Warning! Invalid Credentials!')
            return redirect('login')
            
    else:
       return render(request, 'login.html') 
    
        
        
    
    
