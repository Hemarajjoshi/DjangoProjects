from django.urls import path
from .  import views


urlpatterns = [
    path('', views.home , name = 'home'),
    path('events/', views.events , name = 'events'),
    path('registration/', views.registration, name = 'registration')
]