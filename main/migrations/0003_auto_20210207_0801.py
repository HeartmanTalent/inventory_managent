# Generated by Django 3.1.6 on 2021-02-07 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210206_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='barcode',
            field=models.CharField(max_length=12, unique=True, verbose_name='Barcode'),
        ),
    ]
