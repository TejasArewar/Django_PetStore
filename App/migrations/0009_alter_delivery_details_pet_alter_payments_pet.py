# Generated by Django 5.1 on 2024-10-15 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_delivery_details_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery_details',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.cart'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.cart'),
        ),
    ]
