from django.core.management.base import BaseCommand
from articlesapp.models import ArticleModel


class Command(BaseCommand):
    help = "Update article."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')
        parser.add_argument('title', type=int, help='Article title')
        parser.add_argument('category', type=int, help='Article category')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        article = ArticleModel.objects.filter(pk=pk).first()
        if article is not None:
            article.title = kwargs.get('title')
            article.category = kwargs.get('category')
            self.stdout.write(f'{article}\n' + article.get_summary())
