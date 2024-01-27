# Generated by Django 4.2.7 on 2023-11-20 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_category_category_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_change',
            field=models.DateField(default=datetime.datetime(2023, 11, 20, 19, 58, 51, 120205)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateField(default=datetime.datetime(2023, 11, 20, 19, 58, 51, 120178)),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='blog_images/', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='название товара'),
        ),
    ]
