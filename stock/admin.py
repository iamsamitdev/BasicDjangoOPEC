from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'description', 'price', 'quantity']
    search_fields = ['name', 'sku']
    list_filter = ['price', 'quantity']
    ordering = ['name']
    fieldsets = (
        (None, {
            'fields': ('name', 'sku', 'description', 'price', 'quantity')
        }),
    )
