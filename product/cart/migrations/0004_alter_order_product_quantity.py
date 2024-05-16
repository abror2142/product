# Generated by Django 5.0.6 on 2024-05-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cart_created_at_alter_cart_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_quantity',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
    ]
