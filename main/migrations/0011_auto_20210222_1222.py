# Generated by Django 3.1.6 on 2021-02-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210222_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=100, unique=True, verbose_name='Description'),
        ),
    ]