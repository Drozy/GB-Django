from django.core.management.base import BaseCommand
from articlesapp.models import AuthorModel


class Command(BaseCommand):
    help = "Delete author."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help="Author's ID")

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        author = AuthorModel.objects.filter(pk=pk).first()
        if author is not None:
            author.delete()
            self.stdout.write(f'{author} deleted.')
