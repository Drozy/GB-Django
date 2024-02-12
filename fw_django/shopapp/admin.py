from django.contrib import admin

from .models import Client, Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock']
    ordering = ['-price', 'stock']
    list_filter = ['price']
    search_fields = ['description']
    search_help_text = 'Search product by description'


admin.site.register(Client)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
