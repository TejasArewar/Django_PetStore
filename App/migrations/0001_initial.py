# Generated by Django 5.1 on 2024-10-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cust_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('city', models.CharField(max_length=100, unique=True)),
                ('state', models.CharField(max_length=15)),
                ('pincode', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
