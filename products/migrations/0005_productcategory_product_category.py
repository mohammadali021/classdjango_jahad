# Generated by Django 5.0.7 on 2024-08-22 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('slug', models.SlugField(default='', verbose_name='اسلاگ')),
            ],
            options={
                'verbose_name': 'دسته بندی محصولات',
                'verbose_name_plural': 'دسته بندی محصولات',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='products.productcategory', verbose_name='دسته بندی '),
        ),
    ]