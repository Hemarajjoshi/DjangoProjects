from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('login/', views.login_user, name = 'login_user'),
    path('logout/', views.logout_user, name = 'logout'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('register/', views.register, name = 'register')

    
   
   
   ]
