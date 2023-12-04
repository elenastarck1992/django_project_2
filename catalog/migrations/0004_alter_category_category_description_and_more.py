# Generated by Django 4.2.7 on 2023-11-20 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_category_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.TextField(blank=True, null=True, verbose_name='описание категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_change',
            field=models.DateField(default=datetime.datetime(2023, 11, 20, 18, 34, 1, 75484)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateField(default=datetime.datetime(2023, 11, 20, 18, 34, 1, 75478)),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='', verbose_name='описание товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, verbose_name='название товара'),
        ),
    ]