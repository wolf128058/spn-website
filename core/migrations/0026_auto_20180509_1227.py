# Generated by Django 2.0.4 on 2018-05-09 10:27

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20180508_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='key',
            field=models.CharField(default=core.models.create_key, max_length=100),
        ),
    ]