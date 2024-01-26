import datetime

from django.conf import settings
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='название товара')
    description = models.TextField(default='', verbose_name='описание товара', null=True, blank=True)
    image = models.ImageField(upload_to='products_images/', verbose_name='изображение', null=True, blank=True)
    category = models.ForeignKey('Category', default=None, null=True, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    date_of_creation = models.DateField(default=datetime.datetime.now())
    date_of_change = models.DateField(default=datetime.datetime.now())

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='продавец')

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


class Contact(models.Model):
    phone_number = models.IntegerField(null=True, blank=True, verbose_name='контактный телефон')
    email = models.CharField(max_length=40, null=True, blank=True, verbose_name='электронный адрес')

    class Meta:
        verbose_name = 'Контакты'


class Version(models.Model):
    product_name = models.ForeignKey('Product', blank=True, on_delete=models.CASCADE, verbose_name='Название продукта')
    version_number = models.TextField(max_length=100, default='', verbose_name='Номер версии')
    version_name = models.TextField(max_length=100, default='', null=True, blank=True, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name=' Текущая версия')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f'{self.product_name} версия {self.version_name}-{self.version_number}-{self.is_active}'
