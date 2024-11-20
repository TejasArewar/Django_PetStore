# Generated by Django 5.1 on 2024-10-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='grand_total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
