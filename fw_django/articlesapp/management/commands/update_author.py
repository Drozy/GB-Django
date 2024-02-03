from django.core.management.base import BaseCommand
from articlesapp.models import AuthorModel


class Command(BaseCommand):
    help = "Update author."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help="Author's ID")
        parser.add_argument('firstname', type=str, help="Author's firstname")
        parser.add_argument('lastname', type=str, help="Author's lastname")
        # parser.add_argument('email', type=str, help="Author's Email")
        # parser.add_argument('bio', type=str, help="Author's biography")
        # parser.add_argument('dob', type=str, help="Author's date of birth")

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        author = AuthorModel.objects.filter(pk=pk).first()
        if author is not None:
            author.firstname = kwargs.get('firstname')
            author.lastname = kwargs.get('lastname')
            self.stdout.write(f'{author}')
