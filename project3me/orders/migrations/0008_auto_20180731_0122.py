# Generated by Django 2.0.7 on 2018-07-31 01:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20180731_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='Date',
            field=models.DateField(verbose_name=datetime.datetime(2018, 7, 31, 1, 22, 13, 14062)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Toppings',
            field=models.ManyToManyField(blank=True, to='orders.Toppings'),
        ),
    ]
