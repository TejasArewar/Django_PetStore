# Generated by Django 5.1 on 2024-10-05 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cust_register',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
