# Generated by Django 5.0.6 on 2024-05-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_image_alter_measurement_symbol'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
