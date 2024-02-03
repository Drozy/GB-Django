from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum

from articlesapp.models import AuthorModel


class Command(BaseCommand):
    help = "Create author."

    def handle(self, *args, **kwargs):
        author = AuthorModel(firstname='John', lastname='Weak', email='john@example.com',
                             bio=lorem_ipsum.paragraph(), dob='1980-11-12')
        author.save()
        self.stdout.write(f'{author}')
