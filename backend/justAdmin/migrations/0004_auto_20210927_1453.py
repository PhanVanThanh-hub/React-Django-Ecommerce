# Generated by Django 3.2.6 on 2021-09-27 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justAdmin', '0003_alter_income_data_create'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='growth_total_cost',
        ),
        migrations.RemoveField(
            model_name='income',
            name='growth_total_profit',
        ),
        migrations.RemoveField(
            model_name='income',
            name='growth_total_revenue',
        ),
        migrations.AlterField(
            model_name='income',
            name='data_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
