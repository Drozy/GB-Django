from django.urls import path
from .views import ClientOrders, OrderedProducts

urlpatterns = [
    path('orders/<int:client_id>', ClientOrders.as_view(), name='client_orders'),
    path('products/<int:client_id>', OrderedProducts.as_view(), name='ordered_products'),
]
