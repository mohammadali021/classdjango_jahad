# Generated by Django 5.0.7 on 2024-08-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_productinfo_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfo',
            name='slug',
            field=models.SlugField(default='', verbose_name='اسلاگ'),
        ),
    ]