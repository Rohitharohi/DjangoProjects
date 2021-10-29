# Generated by Django 3.2.8 on 2021-10-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_name', models.CharField(max_length=50, unique=True)),
                ('color', models.CharField(max_length=70)),
                ('ram', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('availability', models.PositiveIntegerField()),
                ('images', models.ImageField(null=True, upload_to='images')),
            ],
        ),
    ]
