# Generated by Django 5.0 on 2024-06-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembros',
            name='password1',
            field=models.CharField(default=1, max_length=340),
            preserve_default=False,
        ),
    ]