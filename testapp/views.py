from django.shortcuts import render, redirect
from .forms import CreateUserForm, loginForm
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login, logout


# Create your views here.

def home(request):
    return render(request, 'testapp/home.html')

def dashboard(request):
    return render(request, 'testapp/dashboard.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Welcome to the website you have been successfully registered.")
            return redirect("login_user")
            
    return render(request, 'testapp/register.html', context = { 'register_form': form})

def login_user(request):
    form = loginForm()
    if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username = username , password = password )
            if user is not None:
                login(request, user)
                messages.success(request, " Succesfully logged in" )
                return redirect("dashboard")
                
            else:
                messages.success(request, "Please Enter valid Username and Password. ")
                return redirect('login_user')
                
    
    return render(request, 'testapp/login.html', context = {'form' : form})
    
def logout_user(request):
    logout(request)
    return redirect("home")