# Generated by Django 3.2.6 on 2021-09-13 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_rename_state_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
