# Generated by Django 2.2.2 on 2020-02-10 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0016_teacher_join_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='join_year',
        ),
    ]