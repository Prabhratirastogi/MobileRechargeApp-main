from django.db import models
from UserAccount.models import *
import datetime
from phonenumber_field.modelfields import PhoneNumberField

class PhoneNumberModel(models.Model):
    user = models.ForeignKey(UserModel, verbose_name="User", on_delete=models.CASCADE)
    phone_number=PhoneNumberField()
    def __str__(self):
        return f"{self.phone_number}" 
class RechargePack(models.Model):
    recharge_price=models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.recharge_price}"
    
class GetRecharge(models.Model):
    recharge_validity=models.IntegerField(null=True,blank=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product=models.ForeignKey(RechargePack,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product}" 
    
class RechargeOrderPlaced(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)
    getrecharge=models.ForeignKey(GetRecharge, on_delete=models.CASCADE)
    phone_number=models.ForeignKey(PhoneNumberModel, on_delete=models.CASCADE)
    ordered_date=models.DateField(default=datetime.date.today,blank=False,null=False)
    STATUS_CHOICES=(
        ('Pending','Pending'),
        ('Accepted','Accepted'),
    )
    status=models.CharField(max_length=150, null=False, blank=False,choices=STATUS_CHOICES,default="Pending")
    
    