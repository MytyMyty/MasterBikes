# Generated by Django 5.0.6 on 2024-06-13 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_alter_product_precio_alter_product_preciod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='precio',
            field=models.DecimalField(decimal_places=3, max_digits=1000),
        ),
    ]
