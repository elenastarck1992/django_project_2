import datetime

from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='название товара')
    description = models.TextField(default='', verbose_name='описание товара', null=True, blank=True)
    image = models.ImageField(upload_to='products_images/', verbose_name='изображение', null=True, blank=True)
    category = models.ForeignKey('Category', default=None, null=True, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    date_of_creation = models.DateField(default=datetime.datetime.now())
    date_of_change = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return f'{self.product_name}  {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='категория товара')
    category_description = models.TextField(verbose_name='описание категории', null=True, blank=True)


    class Meta:
        verbose_name = 'категория товара'
        verbose_name_plural = 'категории товаров'
