# Generated by Django 4.0.5 on 2022-06-19 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20220618_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 19, 17, 15, 27, 30987)),
        ),
    ]