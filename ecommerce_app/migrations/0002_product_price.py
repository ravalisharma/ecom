# Generated by Django 4.2.2 on 2023-06-26 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Price',
            field=models.DecimalField(decimal_places=2, default=39.99, max_digits=20),
        ),
    ]
