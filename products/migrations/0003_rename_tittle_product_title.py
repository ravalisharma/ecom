# Generated by Django 3.2 on 2023-07-05 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='tittle',
            new_name='title',
        ),
    ]
