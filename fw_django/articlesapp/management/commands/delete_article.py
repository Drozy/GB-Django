from django.core.management.base import BaseCommand
from articlesapp.models import ArticleModel


class Command(BaseCommand):
    help = "Delete article."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        article = ArticleModel.objects.filter(pk=pk).first()
        if article is not None:
            article.delete()
            self.stdout.write(f'{article} deleted.')
