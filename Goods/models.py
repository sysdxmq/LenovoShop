from django.db import models


from django.db.models.fields import CharField, FloatField, BigAutoField, IntegerField, DateField, TextField
# Create your models here.

class Goods(models.Model):
	gid=models.BigAutoField(verbose_name="商品ID",primary_key=True);
	name=models.CharField(verbose_name="商品名称",max_length=100);
	price=models.FloatField(verbose_name="价格");
	stock=models.IntegerField(verbose_name="库存");
	release=models.DateField(verbose_name="创建时间");
	showcase=models.TextField(verbose_name="左侧展示图片JSON");
	images=models.TextField(verbose_name="下方展示图片JSON");
	setup=models.TextField(verbose_name="配置单JSON");