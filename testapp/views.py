from django.shortcuts import render, redirect
from .forms import CreateUserForm, loginForm
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
import uuid 


# Create your views here.


#Sending mail function
def send_email(email, token):
  subject = "Please verify the mail before login"
  message = f'Welcome to the website please click the link to verify your email account http://127.0.0.1:8000/verify/{token}'
  from_email = 'thenewhem9845@gmail.com'
  to_email = [email]
  send_mail(subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=to_email)



#Acccount verification function
def account_verify(request, token):
  pf = Profile.objects.filter(token.token).first()
  pf.is_verified = True
  pf.save()


#Home function
@login_required()
def home(request):
  return render(request, 'testapp/home.html')

#Home view
def dashboard(request):
  return render(request, 'testapp/dashboard.html')



# register Function 
def register(request):
  form = CreateUserForm()
  if request.method == "POST":
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      pro_obj = Profile.objects.create(user=user, uid=user.uid)
      pro_obj.save()
      send_email(email = user.email, token = uid )
      
      

      messages.success(
          request,
          "Welcome to the website you have been successfully registered.")
      return redirect("login_user")

  return render(request,
                'testapp/register.html',
                context={'register_form': form})



#login Function
def login_user(request):
  form = loginForm()
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, " Succesfully logged in")
      return redirect("dashboard")

    else:
      messages.success(request, "Please Enter valid Username and Password. ")
      return redirect('login_user')

  return render(request, 'testapp/login.html', context={'form': form})


#logout Function
def logout_user(request):
  logout(request)
  return redirect("home")
