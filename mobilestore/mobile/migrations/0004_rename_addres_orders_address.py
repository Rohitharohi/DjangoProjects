# Generated by Django 3.2.8 on 2021-11-02 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0003_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='addres',
            new_name='address',
        ),
    ]
