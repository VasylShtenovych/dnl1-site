# Generated by Django 2.2.13 on 2021-06-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0020_auto_20210617_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseretrainingteacher',
            name='certificate_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер сертифіката'),
        ),
    ]