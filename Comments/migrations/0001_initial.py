# Generated by Django 3.0 on 2022-11-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('cid', models.BigAutoField(primary_key=True, serialize=False)),
                ('gid', models.IntegerField()),
                ('uid', models.IntegerField()),
                ('oid', models.IntegerField()),
                ('content', models.CharField(max_length=200)),
                ('time', models.DateField()),
                ('stars', models.IntegerField()),
            ],
        ),
    ]
