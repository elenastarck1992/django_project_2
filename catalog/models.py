from django.db import models

class Product(models.Model):
    product_name =models.CharField(max_length=100)
    description = models.TextField
    image = models.ImageField(upload_to='products_images/', verbose_name='изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.IntegerField
    date_of_creation = models.DateField
    date_of_change = models.DateField


    def __str__(self):
        return f'{self.product_name}  {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural= 'товары'

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.TextField
