# Generated by Django 3.2.6 on 2021-09-09 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
        ('cart', '0002_auto_20210908_0946'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='state',
            new_name='region',
        ),
    ]
