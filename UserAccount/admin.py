from django.contrib import admin
from .models import *
# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display=['id','username']
admin.site.register(UserModel,UserModelAdmin)