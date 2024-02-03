from django.core.management.base import BaseCommand
from articlesapp.models import AuthorModel


class Command(BaseCommand):
    help = "Get author by ID."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        author = AuthorModel.objects.filter(pk=pk).first()
        self.stdout.write(f'{author}')
