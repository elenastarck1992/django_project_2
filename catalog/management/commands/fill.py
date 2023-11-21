from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {'product_name': 'чайник Polaris', 'category': Category.objects.create(category_name='Пылесосы'),
             'price': 3000},
            {'product_name': 'cтайлер Dyson', 'category': Category.objects.create(category_name='Стайлеры'),
             'price': 60000}
        ]

        products_for_create = []
        for product_item in product_list:
            products_for_create.append(Product(**product_item))

        Product.objects.bulk_create(products_for_create)
