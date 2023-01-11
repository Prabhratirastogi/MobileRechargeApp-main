from re import A
from django.shortcuts import render
from . serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import time
from django.conf import settings

@api_view(['POST'])
def GetPackView(request):
    if request.method == 'POST':
        user = request.user 
        if user.is_staff==True:
            product_object=RechargePack.objects.create(recharge_price=request.data['recharge_price'],description=request.data['description'])
            product_object.save() 
            getrecharge=GetRecharge.objects.create(user=user,product=product_object,recharge_validity=request.data['recharge_validity'])
            getrecharge.save()
            serializers=GetPackSerializer(getrecharge) 
            return Response({'message': 'Success'},status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'You Have No Permission'},status=status.HTTP_400_BAD_REQUEST) 
            
@api_view(['POST'])
def GetPhoneNumberView(request):
    if request.method == 'POST':
        user = request.user
        if user.is_staff==True:
            phone_number=request.data['phone_number']
            reg = PhoneNumberModel(user=user, phone_number=phone_number)
            reg.save()
            return Response({"messege":"Succesfully Added"},status=status.HTTP_200_OK)
        return Response({'message': 'You Have No Permission'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def RechargeCheckout(request):
    if request.method == 'POST':
        user = request.user
        if user.is_staff==True:
            user_phone_id = request.data['user_phone_id']
            user_details = PhoneNumberModel.objects.filter(id=user_phone_id).order_by('-id').first()
            getrecharge = GetRecharge.objects.filter(user=user)
            for x in getrecharge:
                r=RechargeOrderPlaced.objects.create(user=user,getrecharge=x,phone_number=user_details)
                r.save()
                return Response({"messege":"Your Request for Order has been sent"},status=status.HTTP_200_OK)
                
        return Response(status=status.HTTP_400_BAD_REQUEST)   