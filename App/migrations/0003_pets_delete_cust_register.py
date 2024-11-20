# Generated by Django 5.1 on 2024-10-05 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_cust_register_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('age', models.IntegerField()),
                ('breed', models.CharField()),
                ('gender', models.CharField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Cust_register',
        ),
    ]