from django.db import models
from django.contrib.auth.models import AbstractUser


    
class UserModel(AbstractUser):
    username=models.CharField(max_length=150,null=False, blank=False,unique=True)
    password=models.CharField(max_length=150,null=False, blank=False)
    
    
    USERNAME_FIELD="username"
    PASSWORD_FIELD="password"
