# Generated by Django 2.2.2 on 2019-07-24 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0005_auto_20190723_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
