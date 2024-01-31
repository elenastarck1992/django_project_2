from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import index_contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    VersionCreateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', index_contacts, name='index_contacts'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create/', never_cache(ProductCreateView.as_view()), name='create_product'),
    path('edit/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='edit_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('version_create/', VersionCreateView.as_view(), name='version_create')
]
