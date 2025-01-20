from django.shortcuts import render,redirect
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request,"index.html",{})



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
     
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
             messages.info(request,'Email already taken')
             return redirect('signup')
        else:
            user = User.objects.create_user(username = username, email=email,password=password)
            user.save();
            return redirect('signin')
    
    else:
        return render(request,'signup.html')
            
    
def signin(request):
    if request.method == 'POST':
         uname = request.POST['uname']
         password = request.POST['password']
         user = auth.authenticate(username=uname,password=password)
         if user is not None:
             login(request,user)
             return redirect('home')
         else:
              messages.info(request,'Invalid Credintial')
              return redirect('signin')

    else:
        return render(request,"signin.html")
       

def UserLogout(request):
    logout(request)
    return redirect('signin')


