from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',UserSignupView),
    #http://localhost:8000/user/signup/
    
    path('login/',LoginView),
    #http://localhost:8000/user/login/
]