# Generated by Django 2.1.4 on 2019-06-01 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190601_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 16, 8, 17, 497243), verbose_name='创建时间'),
        ),
    ]