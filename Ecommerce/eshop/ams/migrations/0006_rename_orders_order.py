# Generated by Django 4.2.7 on 2023-11-20 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0005_orders_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
