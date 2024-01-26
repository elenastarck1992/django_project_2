from django.contrib import admin

from catalog.models import Product, Category, Contact, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_filter = ('category_name',)
    search_fields = ('category_name', 'category_description',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category', 'price')
    search_fields = ('product_name', 'description',)

@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email',)

# @admin.register(Version)
# class VersionAdmin(admin.ModelAdmin):
#     list_display = ('product_name', 'version_number', 'version_name', 'current_version_indicator')
#     list_filter = ('current_version_indicator')
