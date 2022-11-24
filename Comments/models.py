from django.db import models

from django.db.models.fields import CharField, DecimalField, TextField, BigAutoField, IntegerField, DateField
# Create your models here.

class Comments(models.Model):
	cid=models.BigAutoField(verbose_name="评论ID",primary_key=True);
	gid=models.IntegerField(verbose_name="商品ID");
	uid=models.IntegerField(verbose_name="用户ID");
	oid=models.IntegerField(verbose_name="订单ID");
	content=models.CharField(verbose_name="评论内容",max_length=200);
	time=models.DateField(verbose_name="评论时间");
	stars=models.IntegerField(verbose_name="评论星级");