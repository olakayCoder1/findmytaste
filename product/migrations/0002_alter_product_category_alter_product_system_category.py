# Generated by Django 5.1.5 on 2025-02-14 22:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, help_text='The vendor category of this product.', null=True, on_delete=django.db.models.deletion.CASCADE, to='product.vendorcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='system_category',
            field=models.ForeignKey(blank=True, help_text='The system category to which this product belongs.', null=True, on_delete=django.db.models.deletion.CASCADE, to='product.systemcategory'),
        ),
    ]
