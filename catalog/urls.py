from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index_contacts, index, product

app_name = CatalogConfig

urlpatterns = [
    path('', index, name='index'),
    path('contact/', index_contacts, name='index_contacts'),
    path('products/<int:pk>', product,  name='product')
]
