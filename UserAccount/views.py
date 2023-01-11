from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

@api_view(['POST']) 
def UserSignupView(request):
   if request.method == 'POST':
        username=request.data['username']
        password=request.data['password']
        
        user_obj=UserModel.objects.filter(username=username)
        if user_obj.exists():
            return Response({"messege":"You are already Registered"},status=status.HTTP_400_BAD_REQUEST)
        user_obj=UserModel.objects.create(username=username)
        user_obj.set_password(password)
        user_obj.is_admin=False
        user_obj.is_superuser=False
        user_obj.is_staff=True
        user_obj.save()
        return Response({"messege":"Account created successfully"},status=status.HTTP_201_CREATED)
    
@api_view(['POST']) 
def LoginView(request):  
    if request.method == 'POST':
        username=request.data['username']
        password=request.data['password'] 
        if UserModel.objects.filter(username=username).exists() :
            u=get_user_model().objects.get(username=username)
            haspassword=u.password
            if check_password(password, haspassword):
                user_obj=authenticate(username=username,password=password)     
                refresh=RefreshToken.for_user(user_obj)
                return Response({
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "messege":"Login successfully"
                })
        else:
            return Response({"messege":"Account not found"},status=status.HTTP_400_BAD_REQUEST)