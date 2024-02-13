from django.urls import path
from .views import ClientOrders, OrderedProducts, ProductView, ProductAdd

urlpatterns = [
    path('orders/<int:client_id>', ClientOrders.as_view(), name='client_orders'),
    path('products/<int:client_id>', OrderedProducts.as_view(), name='ordered_products'),
    path('product/<int:product_id>', ProductView.as_view(), name='product'),
    path('product/add', ProductAdd.as_view(), name='product_add'),
]
