# Generated by Django 4.2.7 on 2023-11-24 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_price',
            new_name='total_price2',
        ),
    ]
