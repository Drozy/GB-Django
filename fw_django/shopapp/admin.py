from django.contrib import admin

from .models import Client, Product, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock']
    ordering = ['-price', 'stock']
    list_filter = ['price']
    search_fields = ['description']
    search_help_text = 'Search product by description'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    readonly_fields = ['reg_date']
    search_fields = ['name', 'email', 'phone_number']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'owner', 'get_total_cost']
    readonly_fields = ['created', 'get_total_cost']
    inlines = [OrderItemInline]
    list_filter = ['owner']
