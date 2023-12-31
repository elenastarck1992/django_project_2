# Generated by Django 4.2.7 on 2023-11-21 18:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_product_date_of_change_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.TextField(blank=True, null=True, verbose_name='описание категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_change',
            field=models.DateField(default=datetime.datetime(2023, 11, 21, 17, 51, 13, 80813)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateField(default=datetime.datetime(2023, 11, 21, 17, 51, 13, 80806)),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='описание товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products_images/', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, verbose_name='название товара'),
        ),
    ]
