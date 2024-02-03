from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from random import randint, choice

from shopapp.models import Client, Product, Order, OrderItem


class Command(BaseCommand):
    help = "Generate fake clients and products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of fakes')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        products = []
        for i in range(1, count + 1):
            product = Product(name=f'Product_{i}',
                              description=lorem_ipsum.sentence(),
                              price=randint(1, 10) * 50.00, stock=randint(5, 20))
            products.append(product)
            product.save()
        for i in range(1, count + 1):
            client = Client(name=f'Client_{i}', email=f'client{i}@example.com', phone_number=f'+799912345{i}')
            client.save()
            order = Order(owner=client)
            order.save()
            for k in range(1, 3):
                some_product = choice(products)
                order_item = OrderItem(order=order, product=some_product, price=some_product.price, quantity=k)
                order_item.save()
