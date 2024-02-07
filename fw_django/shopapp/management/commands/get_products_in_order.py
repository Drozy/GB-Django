from django.core.management.base import BaseCommand

from shopapp.models import Order


class Command(BaseCommand):
    help = "Get products in order by order id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            intro = f'Products in {order}:\n'
            text = '\n'.join((str(item.quantity) + 'x ' + str(item.product) + '\t' +
                              str(item.get_cost())) for item in order.items.all())
            outro = f'\nTotal:\t\t{order.get_total_cost()}'
            self.stdout.write(f'{intro}{text}{outro}')
