# Generated by Django 2.2.10 on 2020-07-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0018_auto_20200301_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='fathers_name',
            field=models.CharField(default='1', max_length=20, verbose_name='По батькові'),
        ),
    ]
