# Generated by Django 5.1.5 on 2025-07-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_rider_document_status_alter_rider_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
