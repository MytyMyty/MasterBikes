# Generated by Django 5.0.6 on 2024-06-12 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=29),
        ),
        migrations.AlterField(
            model_name='product',
            name='precio',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='preciod',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
    ]
