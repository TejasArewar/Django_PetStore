# Generated by Django 5.1 on 2024-10-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_pets_delete_cust_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pets',
            name='image',
            field=models.ImageField(upload_to='pets/'),
        ),
    ]
