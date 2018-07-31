# Generated by Django 2.0.7 on 2018-07-29 23:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20180729_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='Date',
            field=models.DateField(verbose_name=datetime.datetime(2018, 7, 29, 23, 1, 46, 711633)),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='Price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
        ),
    ]
