# Generated by Django 2.2.2 on 2019-07-23 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0002_auto_20190723_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='static/photogallery'),
        ),
    ]
