# Generated by Django 2.1.4 on 2019-06-03 02:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190601_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 3, 10, 53, 8, 128335), verbose_name='创建时间'),
        ),
    ]
