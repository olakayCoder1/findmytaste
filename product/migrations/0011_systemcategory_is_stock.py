# Generated by Django 5.1.5 on 2025-07-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_order_delivered_at_order_delivery_otp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemcategory',
            name='is_stock',
            field=models.BooleanField(default=False),
        ),
    ]
