from django.urls import path
from .views import *
urlpatterns = [
    path('choosepack/',GetPackView),
    #http://localhost:8000/recharge/choosepack/
    path('getphonenumber/',GetPhoneNumberView),
    #http://localhost:8000/recharge/getphonenumber/
    path('requestforrecharge/',RechargeCheckout),
    #http://localhost:8000/recharge/requestforrecharge/
]