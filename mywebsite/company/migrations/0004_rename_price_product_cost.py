# Generated by Django 3.2 on 2021-10-03 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_rename_cost_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='cost',
        ),
    ]
