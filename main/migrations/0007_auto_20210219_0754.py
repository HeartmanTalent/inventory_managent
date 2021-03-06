# Generated by Django 3.1.6 on 2021-02-19 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210209_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispatch',
            fields=[
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date and Time')),
                ('initial_quatity', models.IntegerField(default=10, verbose_name='Initial Quantity')),
                ('quantity', models.IntegerField(default=10, verbose_name='Quantity')),
                ('new_quatity', models.IntegerField(default=10, verbose_name='New Quantity')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(choices=[('sales', 'Sales'), ('stock', 'Stock Transfer ')], default='add', max_length=30, verbose_name='Transaction Type')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.item')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.store')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Purchase',
                'verbose_name_plural': 'Purchases',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date and Time')),
                ('initial_quatity', models.IntegerField(default=10, verbose_name='Initial Quantity')),
                ('quantity', models.IntegerField(default=10, verbose_name='Quantity')),
                ('new_quatity', models.IntegerField(default=10, verbose_name='New Quantity')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(choices=[('purchase', 'Purchase'), ('stock', 'Stock Transfer')], default='add', max_length=30, verbose_name='Transaction Type')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.item')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.store')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Purchase',
                'verbose_name_plural': 'Purchases',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='DispatchedBy',
            fields=[
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date and Time')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date and Time')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('outlet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.outlet')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.store')),
                ('transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.dispatch')),
            ],
            options={
                'ordering': ['-date_modified'],
            },
        ),
        migrations.AlterField(
            model_name='invoice',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.dispatch'),
        ),
        migrations.AlterField(
            model_name='recipt',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.purchase'),
        ),
        migrations.AlterField(
            model_name='suppliedby',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.purchase'),
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
