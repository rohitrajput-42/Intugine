# Generated by Django 3.1.2 on 2020-11-26 08:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]