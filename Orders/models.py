from django.db import models

from django.db.models.fields import CharField, FloatField, BigAutoField, IntegerField, DateField, TextField
# Create your models here.

class Orders(models.Model):
	oid=models.BigAutoField(verbose_name="订单ID",primary_key=True);
	gid=models.IntegerField(verbose_name="商品ID");
	uid=models.IntegerField(verbose_name="用户ID");
	quantity=models.IntegerField(verbose_name="数量");
	status=models.IntegerField(verbose_name="订单状态")
	#在这里面，status表明这个订单属于什么状态。
	#0是购物车状态
	#1是已下单，待支付状态
	#2是已支付，待交货状态
	#3是已完成状态
	#也许会增加退款，取消订单之类的功能，可扩展，再议、
