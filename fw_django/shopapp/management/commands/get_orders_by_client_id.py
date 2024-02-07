from django.core.management.base import BaseCommand

from shopapp.models import Client, Order


class Command(BaseCommand):
    help = "Get all orders by client id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            orders = Order.objects.filter(owner=client)
            intro = f'All orders of {client.name}\n'
            text = '\n'.join(str(order) + ': ' + str(order.get_total_cost()) for order in orders)
            self.stdout.write(f'{intro}{text}')
