from django.shortcuts import render, redirect
from  .forms import ViewerRegistrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login, logout

# Create your views here.
def home(request):
    form = LoginForm()
    return render(request, 'testapp/home.html', {'form' : form})

def events(request):
    return render(request,'testapp/events.html')

def registration(request):
    form = ViewerRegistrationForm()
    if request.method == "POST":
        form = ViewerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome </b>{user.username}<b>. You have been successfully registered.')
            return redirect("events")

    return render(request, 'testapp/registration.html', {'form': form})