# Generated by Django 5.0.6 on 2024-07-03 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0028_product_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='redondeo',
            field=models.DecimalField(decimal_places=3, default=0.09, max_digits=5),
        ),
    ]
