# Generated by Django 3.0 on 2022-11-20 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='cid',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='评论ID'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.CharField(max_length=200, verbose_name='评论内容'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='gid',
            field=models.IntegerField(verbose_name='商品ID'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='oid',
            field=models.IntegerField(verbose_name='订单ID'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='stars',
            field=models.IntegerField(verbose_name='评论星级'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.DateField(verbose_name='评论时间'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='uid',
            field=models.IntegerField(verbose_name='用户ID'),
        ),
    ]