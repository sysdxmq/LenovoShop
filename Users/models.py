from django.db import models

# Create your models here.
class Users(models.Model):
	uid=models.BigAutoField(verbose_name="用户ID",primary_key=True)
	phone=models.CharField(verbose_name="用户手机",max_length=20)
	password=models.CharField(verbose_name="明文密码",max_length=32)
	address=models.CharField(verbose_name="地址",max_length=200)
	username=models.CharField(verbose_name="用户名",max_length=32)