# Generated by Django 3.0 on 2022-11-20 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='gid',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='商品ID'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='images',
            field=models.TextField(verbose_name='下方展示图片JSON'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=100, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.FloatField(verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='release',
            field=models.DateField(verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='setup',
            field=models.TextField(verbose_name='配置单JSON'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='showcase',
            field=models.TextField(verbose_name='左侧展示图片JSON'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='stock',
            field=models.IntegerField(verbose_name='库存'),
        ),
    ]