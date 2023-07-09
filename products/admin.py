from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'product_name', 'quantity', 'categories', 'packaging', 'brands']
