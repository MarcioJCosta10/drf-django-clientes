# Generated by Django 3.0.8 on 2022-06-18 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20200806_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 18, 17, 49, 57, 565134)),
        ),
    ]
