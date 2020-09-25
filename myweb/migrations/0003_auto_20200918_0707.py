# Generated by Django 2.2.7 on 2020-09-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0002_auto_20200918_0611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmanager',
            name='Role',
        ),
        migrations.AddField(
            model_name='groupmanager',
            name='Email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='groupmanager',
            name='Nickname',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='groupmanager',
            name='Phone',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
