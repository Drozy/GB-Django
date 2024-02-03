from django.core.management.base import BaseCommand
from articlesapp.models import ArticleModel


class Command(BaseCommand):
    help = "Get all articles."

    def handle(self, *args, **kwargs):
        articles = ArticleModel.objects.all()
        self.stdout.write(f'{articles}')
