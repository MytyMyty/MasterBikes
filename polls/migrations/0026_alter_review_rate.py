# Generated by Django 5.0.6 on 2024-06-25 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_alter_review_product_alter_review_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(choices=[(None, 'Ninguna'), (1, 'Uno'), (2, 'Dos'), (3, 'Tres'), (4, 'Cuatro'), (5, 'Cinco')], default=None),
        ),
    ]