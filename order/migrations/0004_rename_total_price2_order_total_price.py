# Generated by Django 4.2.7 on 2023-11-24 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_rename_total_price_order_total_price2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_price2',
            new_name='total_price',
        ),
    ]