from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum

from articlesapp.models import ArticleModel, AuthorModel


class Command(BaseCommand):
    help = "Create article."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = AuthorModel.objects.filter(pk=pk).first()
        if author is not None:
            article = ArticleModel(title='Пробная статья', content=lorem_ipsum.paragraph(),
                                   author=author, category='Тестовая категория')
            article.save()
            self.stdout.write(f'{article}')
        else:
            self.stdout.write(f'Автор с id={pk} не найден.')
