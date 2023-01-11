from django.contrib import admin
from .models import *
# Register your models here.
class PhoneNumberModelAdmin(admin.ModelAdmin):
    list_display=['id','user','phone_number']
admin.site.register(PhoneNumberModel,PhoneNumberModelAdmin)

class RechargeAdmin(admin.ModelAdmin):
    list_display=['id','recharge_price','description']
admin.site.register(RechargePack,RechargeAdmin)

class GetRechargeAdmin(admin.ModelAdmin):
    list_display=['id','recharge_validity','user','product']
admin.site.register(GetRecharge,GetRechargeAdmin)

class RechargeOrderPlacedAdmin(admin.ModelAdmin):
    list_display=['id','user','getrecharge','phone_number','ordered_date','status']
admin.site.register(RechargeOrderPlaced,RechargeOrderPlacedAdmin)