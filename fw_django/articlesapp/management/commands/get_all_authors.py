from django.core.management.base import BaseCommand
from articlesapp.models import AuthorModel


class Command(BaseCommand):
    help = "Get all authors."

    def handle(self, *args, **kwargs):
        authors = AuthorModel.objects.all()
        self.stdout.write(f'{authors}')
