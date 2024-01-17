from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index_contacts, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', index_contacts, name='index_contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    # path('product/create', ProductCreateView.as_view(),  name='create_products')
]
